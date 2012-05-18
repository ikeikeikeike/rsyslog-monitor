# -*- coding: utf-8 -*-
import os
import re
import time

from django.template import RequestContext as RC
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.db.models import Q
from django_websocket import accept_websocket

from . import models as mdl
from . import utils
from . import decorators


# persistent variables
message_list = []
websocket_list = []


@accept_websocket
def websocket(request):
    #: TODO multiple log
    logfile = open(mdl.Source.objects.get(pk=1).path)
    loglines = utils.follow(logfile)

    websocket_list.append(request.websocket)
    for line in loglines:
        for ws in websocket_list:
            ws.send(line)


@accept_websocket
def tail(request):
    """ tail buffer """
    logfile = open(mdl.Source.objects.get(pk=1).path)
    loglines = utils.follow(logfile)

    for msg in request.websocket:
        ptn = re.compile(utils.modify_message(msg))
        for line in loglines:
            if ptn.search(line):
                request.websocket.send(line)


@accept_websocket
def fetch(request):
    """ search storage """
    def cs(l):
        return u"{r} {f} {s} {m}".format(
            r=l.get("receivedat").strftime("%b %d %X"),
            f=l.get("fromhost"),
            s=l.get("syslogtag"),
            m=l.get("message")
        )

    for msg in request.websocket:
        m = utils.modify_message(msg)
        data = mdl.Systemevents.objects.filter(
            # Q(receivedat__contains=m) |
            Q(syslogtag__contains=m) |
            Q(fromhost__contains=m) |
            Q(message__contains=m)
        ).values("receivedat", "fromhost", "syslogtag", "message")
        #[0:20]
        for i, s in enumerate(map(cs, data[::-1])):
            if (i % 10) == 0:
                time.sleep(0.1)
            request.websocket.send(s)


def required(request):
    path = request.POST.get("path")
    if (path and os.access(path.decode("utf-8"), os.R_OK)
             and os.path.isfile(path.decode("utf-8"))
             and path.decode("utf-8") in ["/var/log/rsyslog", "/var/log/syslog", "/var/log/message"]):
        #: TODO multiple log
        obj, created = mdl.Source.objects.get_or_create(path=path)
        return HttpResponseRedirect(reverse("rsyslogmonitor_index"))
    return render_to_response('rsyslogmonitor/required.html', RC(request, {
        "path": path
    }))


@decorators.syslog_required(lambda request, *args, **kwargs: True if 0 < mdl.Source.objects.count() else False)
def index(request):
    return render_to_response('rsyslogmonitor/websocket.html', RC(request, {}))


# vim: set et fenc=utf-8 ft=python ff=unix sts=4 sw=4 ts=4 :

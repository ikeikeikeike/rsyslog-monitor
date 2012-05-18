# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url  # , include
from . import views

urlpatterns = patterns('',
    url(r"^$", views.index, name="rsyslogmonitor_index"),
    url(r"^fetch/$", views.fetch, name="rsyslogmonitor_fetch"),
    url(r"^tail/$", views.tail, name="rsyslogmonitor_tail"),
    url(r"^websocket/$", views.websocket, name="rsyslogmonitor_websocket"),
    url(r"^required/$", views.required, name="rsyslogmonitor_required"),
)


# vim: set et fenc=utf-8 ft=python ff=unix sts=4 sw=4 ts=4 :

``A Django rsyslog monitor``

Description
===========
Django rsyslog monitor

Requirements
============
* django
* django-wesocket

Features
========
* search In realtime - from a browser.
* tail search.
* Database search.
* Multiple Host.
* Django Base System.
* using WebSocket.
* support syslog and rsyslog.

Setup
=====
::

    $ pip install git+git://github.com/ikeikeikeike/rsyslog-monitor.git

Installation
~~~~~~~~~~~~

edit settings.py ::

    INSTALLED_APPS = (
        "django_websocket",
        "rsyslogmonitor",
    )


edit urls.py ::

    urlpatterns = patterns('',
        url(r'^rsyslogmonitor/', include("rsyslogmonitor.urls")),
    )

Multiple Host Setting
~~~~~~~~~~~~~~~~~~~~~~~
edit (r)syslog.conf at send server. ::

    $ cat /etc/syslog.conf
    ### Configuration file for rsyslog or syslog
    ### Changes are preserved
    # for tcp
    ### *.*          @@192.168.100.41:514
    # for udp
    *.*          @192.168.100.85:514


History
========
0.1 (2012-5-18)
~~~~~~~~~~~~~~~~
* first release

0.x (201x-xx-xx)
~~~~~~~~~~~~~~~~~
* replace to Comet from WebSocket.
* replace to Tornado from Django Base System.
* support log Analysis and Visualization of Metrics.

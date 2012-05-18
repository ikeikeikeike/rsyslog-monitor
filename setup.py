import os
from setuptools import setup

version = '0.1'
name = 'rsyslog-monitor'
short_description = 'A Django rsyslog monitor with WebSocket. search In realtime - from a browser.'
long_description = """\
A Django rsyslog monitor

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

"""


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
extensions_dir = 'rsyslogmonitor'

for dirpath, dirnames, filenames in os.walk(extensions_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])


classifiers = [
   "Development Status :: 3 - Alpha",
   "Development Status :: 4 - Beta",
   "Framework :: Django",
   "Environment :: Web Environment",
   "Intended Audience :: Developers",
   "Programming Language :: Python",
   'Topic :: Utilities',
   'License :: OSI Approved :: MIT License',
]

setup(
    name=name,
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=classifiers,
    keywords=['syslog', 'rsyslog', 'django', 'websocket'],
    author='Tatsuo Ikeda',
    author_email='jp.ne.co.jp at gmail',
    url='https://github.com/ikeikeikeike/rsyslog-monitor',
    license='MIT License',
    packages=packages,
    data_files=data_files,
    py_modules=['rsyslogmonitor'],
    install_requires=['django-websocket', 'django']
)

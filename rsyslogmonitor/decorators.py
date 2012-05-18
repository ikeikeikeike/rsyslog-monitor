# -*- coding: utf-8 -*-
try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import available_attrs
from django.contrib.auth.views import redirect_to_login

REQUIRED_URL = getattr(settings, "RSYSLOGMONITOR_REQUIRED_URL", reverse_lazy("rsyslogmonitor_required"))
REDIRECT_FIELD_NAME = getattr(settings, "RSYSLOGMONITOR_REDIRECT_FIELD_NAME", "rsyslogmonitor_required")


def syslog_required(test_func, redirect_field_name=REDIRECT_FIELD_NAME, settings_url=REQUIRED_URL):
    """ syslog require method """
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request, *args, **kwargs):
                return view_func(request, *args, **kwargs)
            path = request.get_full_path()
            return redirect_to_login(path, settings_url, redirect_field_name)
        return _wrapped_view
    return decorator


# vim: set et fenc=utf-8 ft=python ff=unix sts=4 sw=4 ts=4 :

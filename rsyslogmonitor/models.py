# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models


class Systemevents(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    customerid = models.BigIntegerField(null=True, db_column='CustomerID', blank=True)  # Field name made lowercase.
    receivedat = models.DateTimeField(null=True, db_column='ReceivedAt', blank=True)  # Field name made lowercase.
    devicereportedtime = models.DateTimeField(null=True, db_column='DeviceReportedTime', blank=True)  # Field name made lowercase.
    facility = models.IntegerField(null=True, db_column='Facility', blank=True)  # Field name made lowercase.
    priority = models.IntegerField(null=True, db_column='Priority', blank=True)  # Field name made lowercase.
    fromhost = models.CharField(max_length=180, db_column='FromHost', blank=True)  # Field name made lowercase.
    message = models.TextField(db_column='Message', blank=True)  # Field name made lowercase.
    ntseverity = models.IntegerField(null=True, db_column='NTSeverity', blank=True)  # Field name made lowercase.
    importance = models.IntegerField(null=True, db_column='Importance', blank=True)  # Field name made lowercase.
    eventsource = models.CharField(max_length=180, db_column='EventSource', blank=True)  # Field name made lowercase.
    eventuser = models.CharField(max_length=180, db_column='EventUser', blank=True)  # Field name made lowercase.
    eventcategory = models.IntegerField(null=True, db_column='EventCategory', blank=True)  # Field name made lowercase.
    eventid = models.IntegerField(null=True, db_column='EventID', blank=True)  # Field name made lowercase.
    eventbinarydata = models.TextField(db_column='EventBinaryData', blank=True)  # Field name made lowercase.
    maxavailable = models.IntegerField(null=True, db_column='MaxAvailable', blank=True)  # Field name made lowercase.
    currusage = models.IntegerField(null=True, db_column='CurrUsage', blank=True)  # Field name made lowercase.
    minusage = models.IntegerField(null=True, db_column='MinUsage', blank=True)  # Field name made lowercase.
    maxusage = models.IntegerField(null=True, db_column='MaxUsage', blank=True)  # Field name made lowercase.
    infounitid = models.IntegerField(null=True, db_column='InfoUnitID', blank=True)  # Field name made lowercase.
    syslogtag = models.CharField(max_length=180, db_column='SysLogTag', blank=True)  # Field name made lowercase.
    eventlogtype = models.CharField(max_length=180, db_column='EventLogType', blank=True)  # Field name made lowercase.
    genericfilename = models.CharField(max_length=180, db_column='GenericFileName', blank=True)  # Field name made lowercase.
    systemid = models.IntegerField(null=True, db_column='SystemID', blank=True)  # Field name made lowercase.

    class Meta:
        db_table = u'SystemEvents'
        ordering = ['-id']


class Systemeventsproperties(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    systemeventid = models.IntegerField(null=True, db_column='SystemEventID', blank=True)  # Field name made lowercase.
    paramname = models.CharField(max_length=765, db_column='ParamName', blank=True)  # Field name made lowercase.
    paramvalue = models.TextField(db_column='ParamValue', blank=True)  # Field name made lowercase.

    class Meta:
        db_table = u'SystemEventsProperties'
        ordering = ['-id']


# auto-generated end


class Source(models.Model):
    path = models.CharField(max_length=100)

    def get_path(self, instance, filename):
        return u"{path}".format(path=self.path)

    files = models.FilePathField(path=get_path, match="*.log", recursive=True, blank=True, null=True)



# vim: set et fenc=utf-8 ff=unix sts=4 sw=4 ts=4 :

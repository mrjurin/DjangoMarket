# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    delete_date = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ["pk"]

    def __unicode__(self):
        return self.__str__()


class Accounts(models.Model):
    login = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=60, blank=True)
    mobile_number = models.CharField(max_length=12, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(choices=('male', 'female'))

    def __str__(self):
        return self.login

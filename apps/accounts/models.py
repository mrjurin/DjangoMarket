# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('Email address', unique=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __unicode__(self):
        return self.email


class Account(User):
    login = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=60, blank=True)
    mobile_number = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=100)
    GENDER_CHOICES = ("male", "female")
    gender = models.CharField(choices=GENDER_CHOICES)

    def __unicode__(self):
        return self.login

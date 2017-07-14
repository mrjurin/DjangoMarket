# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    name = models.CharField(max_length=60)
    email = models.EmailField('Email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        # ordering = ['name']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        User.save(*args, **kwargs)


class UserData(models.Model):

    GENDER_CHOICES = (('MA',"male"), ('FE', "female"))

    email = models.ForeignKey('User')
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='accounts/photo', height_field=120, width_field=160)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='')

    class Meta:
        ordering = ['login']
        verbose_name = "userdata"
        verbose_name_plural = "userdata"

    def __unicode__(self):
        return self.login

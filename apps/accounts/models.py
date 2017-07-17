# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_CHOICES = (('MA', "male"), ('FE', "female"))

    name = models.CharField(default='name {}'.format(id), max_length=60)
    email = models.EmailField('Email address', unique=True)
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=13, blank=True)  # +380671111111 - 13 signs
    home_address = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='accounts/photo', height_field=120, width_field=160)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['name']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        User.save(*args, **kwargs)

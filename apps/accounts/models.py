# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_CHOICES = (('UN', 'unknown'), ('MA', "male"), ('FE', "female"))

    # def default_username(self, **kwargs):
    #     context = super(User, self).default_username(**kwargs)
    #     context['username'] = 'user#%s' % self.id
    #     return context['username']

    username = models.CharField(max_length=50, unique=True)
    # username = models.CharField(default=default_username(),
    #                             max_length=50, unique=True)
    password = models.CharField(default='00', max_length=20, blank=True)
    mobile_number = models.CharField(max_length=13, blank=True)  # +380671111111 - 13 signs
    home_address = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='accounts/photo', height_field=120, width_field=160, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='')

    class Meta:
        ordering = ['id']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return '{}#{}'.format(self.username, self.id)

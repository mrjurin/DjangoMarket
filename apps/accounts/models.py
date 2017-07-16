# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    name = models.CharField(default='name', max_length=60)
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

# Не розумію чого не добавити усі ці поля в модель Юзер? Навіщо створювати ще одну?
class UserData(models.Model):

    # Можна зберітаги і повни назви, а не скорочені, та питання, для чього нам ця інфа взагалі?
    GENDER_CHOICES = (('MA',"male"), ('FE', "female"))

    # Чому поле називаєтясь емейл?
    email = models.ForeignKey('User')
    
    # Що таке логін?
    login = models.CharField(max_length=20, unique=True)
    
    password = models.CharField(max_length=20)
    
    # +38(067)1111111 - довжина 16 символів
    mobile_number = models.CharField(max_length=12, blank=True)
    
    # Как сортування по містам роботи
    address = models.CharField(max_length=100, blank=True)
    
    
    photo = models.ImageField(upload_to='accounts/photo', height_field=120, width_field=160)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='')

    class Meta:
        ordering = ['login']
        # Поганий вибір
        verbose_name = "userdata"
        verbose_name_plural = "userdata"

    def __unicode__(self):
        return self.login

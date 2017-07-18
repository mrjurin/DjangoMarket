# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name']
    search_fields = ['name', 'email']

    class Meta:
        model = User

admin.site.register(User)

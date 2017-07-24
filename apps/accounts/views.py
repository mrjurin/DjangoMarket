# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from .models import User


class UsersView(TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)
        context['users'] = User.get_all_users()
        return context

    def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)

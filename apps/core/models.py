# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Order(models.Model):
    article = models.CharField(max_length=45)
    additional_information = models.TextField(max_length=450)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Full price")
    created_date = models.DateTimeField(auto_now_add=True)
    sent_date = models.DateTimeField()
    customer = models.ForeignKey(settings.AUTH_USER_MODEL)
    payment_cash = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.article

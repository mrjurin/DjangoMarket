# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Order(models.Model):
    article = models.CharField(max_length=45)
    description = models.TextField(max_length=450)
    quantity = models.FloatField()
    price = models.DecimalField()
    order_date = models.DateTimeField()
    customer = models.CharField(max_length=100)
    payment_cash = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.article

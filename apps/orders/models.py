# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Order(models.Model):
    product = models.ManyToManyField('', max_length=45)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    coupon = models.ForeignKey('')
# FIXME: PryimaRoman: insert location of other models
    additional_information = models.TextField(max_length=450)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Full price")
    created_date = models.DateTimeField(auto_now_add=True)
    sent_date = models.DateTimeField()
    payment_cash = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.product

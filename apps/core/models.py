# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Cart(models.Model):

    # Cart Model

    class Meta(object):
        verbose_name = u"Cart"
    
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    place_order = models.BooleanField(default=False, verbose_name=_('Place Order'))

    cart_id = models.CharField(max_length=50)
    orders = models.ManyToMnyaField(Order)
    products = models.ManyToMnyaField(Product)
    coupon = models.OneToOneField(Coupon, primary_key=True)
    subtotal = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Subtotal")


    def __unicode__(self):
        return self.cart_id

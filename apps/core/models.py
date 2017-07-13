# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    delete_date = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ["pk"]

    def __unicode__(self):
        return self.__str__()

    
class Cart(models.Model):

    # Cart Model
    
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    place_order = models.BooleanField(default=False, verbose_name=_('Place Order'))

    orders = models.ManyToManyField(Order)
    products = models.ManyToManyField(Product)
    coupon = models.OneToOneField(Coupon, primary_key=True)
    subtotal_amount = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("Subtotal"))

    class Meta(object):
        verbose_name = _("Cart")
        
    def __unicode__(self):
        return self.cart_id

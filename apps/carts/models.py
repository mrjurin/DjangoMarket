# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from ..core.models import BaseModel
from ..orders.models import Order
from ..products.models import Product

   
class Cart(BaseModel):

    # Cart Model
    
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
      
      # для чього це поле?
    place_order = models.BooleanField(default=False, verbose_name=_('Place Order'))

    # поле називається Ордер, але чомусь мени-ту-мени.
    # Для чого взагалі це поле?
    order = models.ManyToManyField(Order)
      
    # Поле продукт, але продуктів може бути багато, краще робити продуктс
    product = models.ManyToManyField(Product)
      
    # кількість чього? 
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
     
    # Не зрозуміло що ми тут будемо зберігати?
    unit_price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("Unit Price"))
   
    # Ось це гуд
    shipping_cost = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("Shipping Cost"))
    tax_cost = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("TAX"))
    subtotal_amount = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("Subtotal"))

    class Meta(object):
        verbose_name = _("Cart")
        ordering = ['create_date']
        
    def __unicode__(self):
        # Поля карт_ід вже нема
        return self.cart_id

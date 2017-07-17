# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from ..products.models import Product
from ..coupons.models import ItemSaleCoupon


class Order(models.Model):
    # Продукт у нас тільки один?
    # Якщо ManyToManyField то, і поле повинно відображати ту ж суть
    # products
    product = models.ManyToManyField(Product) #max_length=45)
    # кул
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    # Кул, додай ще вербосе нейм
    coupon = models.ForeignKey(ItemSaleCoupon, null=True, blank=True)
# FIXME: PryimaRoman: insert location of other models
    additional_information = models.TextField(max_length=450, null=True, blank=True)
    # Кількість чього? продуктів? У нас і так вона є в продуктах 
    quantity = models.PositiveIntegerField(null=True, blank=True)
    
    # Ціна чього? Поле не відображає суті
    # full_price - то вже зрозуміліше
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Full price")
    created_date = models.DateTimeField(auto_now_add=True)
    sent_date = models.DateTimeField()

    # Як булеан може бути пустим?
    payment_cash = models.BooleanField(default=True)

    def __str__(self):
        # Тут щось не зрозуміло взагалі
        return self.product

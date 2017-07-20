# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Cart, ShippingCost, Product


class CartAdmin(admin.ModelAdmin):
    # list_display = ['id', 'Product.name', 'unit_price', 'quantity', 'ShippingCost.shipping_name', 'ShippingCost.value',
    #                 'tax_cost', 'subtotal_amount']
    # list_filter = ['product']
    # search_fields = ['product']
    pass


admin.site.register(Cart, CartAdmin)
admin.site.register(ShippingCost)

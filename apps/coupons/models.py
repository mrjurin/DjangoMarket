# -*- coding: utf-8 -*-
from uuid import uuid4
from datetime import datetime

from django.db import models


percent = 'P'
natural = 'N'
value_types = [percent, natural]


class _CouponBase(models.Model):
    """
    Base coupon model.
    By default all new coupons valid.
    Every model have conditions to set model not valid
    """
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)
    delete_date = models.DateTimeField(null=True, blank=True, db_index=True)

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    coupon_secret = models.CharField(default=uuid4(), editable=False)

    is_valid = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["pk"]

    def __unicode__(self):
        return self.name

# region GiftCoupons
personal_gift = 'P'
mass_gift = 'M'
git_types = [personal_gift, mass_gift]


class GiftCoupon(_CouponBase):
    """
    Gift coupon
    """
    value_type = models.CharField(
        choices=value_types, max_length=1, default=natural, blank=False, null=False,
        editable=False)
    git_type = models.CharField(
        choices=git_types, max_length=1, blank=False, null=False, editable=False)
    value = models.PositiveIntegerField(blank=False)
    expired_date = models.DateTimeField(default=datetime.max)

    class Meta:
        db_table = 'gift_coupon'


class UserGiftCoupon(models.Model):
    """
    User gift coupon additional information
    This coupon can be used once by one user

    """
    GiftCoupon = models.OneToOneField(GiftCoupon, editable=False)
    used_date = models.DateTimeField(blank=True)

    class Meta:
        db_table = 'gift_user'


class PromoGiftCoupon(models.Model):
    """
    Promo gift coupon additional information
    This coupon can be used once by each user
    Coupon not valid after expired_date or can_used <= 0
    """
    GiftCoupon = models.OneToOneField(GiftCoupon, editable=False)
    can_used = models.PositiveIntegerField()  # rename?

    class Meta:
        db_table = 'gift_promo'
# endregion

# region SaleCoupon
item_sale = 'I'
category_sale = 'C'
sale_types = [item_sale, category_sale]


class SaleCoupon(_CouponBase):
    """
    Sale coupon
    Coupon valid only after start date
    Coupon not valid after expired_date
    """
    value_type = models.CharField(
        choices=value_types, max_length=1, default=percent, blank=False, null=False)
    sale_type = models.CharField(
        choices=sale_types, max_length=1, blank=False, null=False)
    default_value = models.PositiveIntegerField(blank=False)

    start_date = models.DateTimeField()
    expired_date = models.DateTimeField()

    class Meta:
        db_table = 'sale_coupon'


class ItemSaleCoupon(SaleCoupon):
    """
    Item sale coupon additional information
    This coupon can be used many times by each user
    Different items can have different sale value
    If value not set used default_value from SaleCoupon class
    """
    sale_coupon_id = models.ForeignKey(SaleCoupon)
    product_id = models.ForeignKey('Product')
    value = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sale_item'


class CategorySaleCoupon(SaleCoupon):
    """
    Category sale coupon additional information
    This coupon can be used many times by each user
    Different item categories can have different sale value
    If value not set used default_value from SaleCoupon class
    """
    sale_coupon_id = models.ForeignKey(SaleCoupon)
    category_id = models.ForeignKey('Category')
    value = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sale_category'
# endregion

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    delete_date = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ["pk"]

    def __unicode__(self):
        return self.__str__()


class Category(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default='', max_length=50, unique=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-create_date']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(default='', max_length=255, unique=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    quantity = models.IntegerField()
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='products')
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, related_name='images')
    image = models.ImageField(upload_to='products/images')
    caption = models.CharField(max_length=200, blank=True)
from django.contrib import admin
from django.template.defaultfilters import slugify

from .models import (Category, Product, ProductImage, Brand,
                     AttributeName, AttributeValue, ProductReview)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    prepopulated_fields = {'slug': ['name']}


    def save_model(self, request, obj, form, change):
        slug = slugify(obj.name)
        if obj.slug != slug:
            obj.slug = slug
        super(ProductAdmin, self).save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(self.name)
        super(CategoryAdmin, self).save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(AttributeName)
admin.site.register(AttributeValue)
admin.site.register(ProductReview)

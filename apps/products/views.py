from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from apps.products.models import Product, Category


class ProductsView(TemplateView):
    template_name = "products.html"

    def products(self):
        return Product.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super(ProductsView, self).get_context_data(**kwargs)
    #     context['products']= Product.objects.all()
    #     return context


class ProductDetailView(DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'
    template_name = 'product_detail.html'


class CategoriesView(TemplateView):
    template_name = "categories.html"

    def categories(self):
        return Category.objects.all()


class CategoryProductsView(TemplateView):
    template_name = "category_products.html"

    def category_products(self):
        category_slug = self.kwargs['category_slug']
        category = Category.objects.get(slug=category_slug)
        return category.category_products.all()


class CategoryDetailView(DetailView):
    model = Category
    slug_url_kwarg = 'category_slug'
    template_name = 'category_detail.html'




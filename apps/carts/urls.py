from django.conf.urls import url

from .views import CartView

urlpatterns = [
    url(r'^cart_view/$', CartView.as_view(), name="cart_view")
]
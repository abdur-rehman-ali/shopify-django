from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('product/detail/<int:id>', views.product_detail, name="product_detail"),
  path('shopping-cart', views.add_to_cart, name="add_to_cart")
]

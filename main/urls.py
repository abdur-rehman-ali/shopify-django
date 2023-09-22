# Django Imports 
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Local Imports 
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('product/detail/<int:id>', views.product_detail, name="product_detail"),
  path('shopping-cart', views.shopping_cart, name="shopping_cart"),
  path('add-to-cart', views.add_to_cart, name="add_to_cart"),
  path('update-cart', views.update_cart),
  path('buy-product', views.buy_now, name="buy_now"),
  path('profile', views.profile, name="profile"),
  path('address', views.address, name="address"),
  path('orders', views.orders, name="orders"),
  path('checkout', views.checkout, name="checkout"),
  path('confirm-order', views.confirm_order, name="confirm_order"),
  path('category/mobile', views.mobile_category, {'data': None}, name="mobile_category_index"),
  path('category/mobile/<slug:data>', views.mobile_category, name="mobile_category"),
  path('category/laptop', views.laptop_category, {'data': None}, name="laptop_category_index"),
  path('category/laptop/<slug:data>', views.laptop_category, name="laptop_category"),
  path('registration', views.registration, name="registration"),
  path('login', views.login, name="login"),
  path('logout', views.logout, name="logout"),
  path('change/password', views.password_change, name="password_change"),
  path('products/new', views.new_product, name="new_product"),
  path('products', views.products, name="products"),
  path('products/<int:product_id>/edit', views.edit_product, name="edit_product"),
  path('products/<int:product_id>/delete', views.delete_product, name="delete_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

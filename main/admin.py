# Django Imports 
from django.contrib import admin

# Local Imports
from .models import (
  Product,
  Address,
  ShoppingCart,
  Order,
  Item
)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'selling_price', 'discounted_price')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
  list_display = ('id', 'street', 'state', 'city', 'country', 'zip_code', 'phone_number', 'user')

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
  list_display = ('id', 'user', 'product', 'quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ('id', 'user', 'address', 'ordered_date', 'status')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
  list_display = ('id', 'order', 'product', 'quantity')

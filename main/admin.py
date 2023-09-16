# Django Imports 
from django.contrib import admin

# Local Imports
from .models import (
  Product,
  Address
)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'selling_price', 'discounted_price')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
  list_display = ('id', 'street', 'state', 'city', 'country', 'zip_code', 'phone_number', 'user')

# Django Imports 
from django.contrib import admin

# Local Imports
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'selling_price', 'discounted_price')

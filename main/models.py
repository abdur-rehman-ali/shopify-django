# Django Imports 
from django.db import models
from django.contrib.auth.models import User

CATEGORIES = (
  ('Mobile','Mobile'),
  ('Laptop','Laptop'),
  ('Top Wear','Top Wear'),
  ('Bottom Wear','Bottom Wear'),
)

class Product(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  selling_price = models.FloatField()
  discounted_price = models.FloatField()
  brand = models.CharField(max_length=100)
  category = models.CharField(choices=CATEGORIES, max_length=50)
  product_image = models.ImageField(upload_to='products_images')

  def __str__(self):
    return str(self.id)

class Address(models.Model):
  street = models.TextField()
  state = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  zip_code = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=20)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')

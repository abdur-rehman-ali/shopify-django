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

  @property
  def formatted_address(self):
    return f"{self.street},  {self.state}, {self.city}, {self.country}"

  def __str__(self):
    return f"{self.id}"

class ShoppingCart(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_products')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
  quantity = models.IntegerField(default=1)

  @property
  def total_cost(self):
    return self.quantity * self.product.discounted_price
  
  class Meta:
    unique_together = ('product', 'user')

STATUS_CHOICES = (
  ('pending', 'Pending'),
  ('accepted', 'Accepted'),
  ('rejected', 'Rejected'),
  ('dispatched', 'Dispatched'),
  ('delivered', 'Delivered'),
)

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
  address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='orders')
  ordered_date = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

  def __str__(self):
    return f"{self.id}"

class Item(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ordered_items')
  quantity = models.IntegerField(default=1)

  @property
  def total_cost(self):
    return self.quantity * self.product.discounted_price

  def __str__(self):
    return f"{self.id}"

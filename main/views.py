from django.shortcuts import render
from .models import Product

def index(request):
  mobiles = Product.objects.filter(category='Mobile')
  laptops = Product.objects.filter(category='Laptop')
  products = Product.objects.all()
  template_name = 'main/index.html'
  context = {
    'mobiles': mobiles,
    'laptops': laptops,
    'products': products
  }
  return render(request, template_name, context)

def product_detail(request, id):
  template_name = 'main/product_detail.html'
  image_url = f"main/images/product/{id}.jpg"
  content = {'id': id, 'image_url': image_url}
  return render(request, template_name, content)

def add_to_cart(request):
  template_name = 'main/add_to_cart.html'
  return render(request, template_name)

def buy_now(request):
  template_name = 'main/buy_now.html'
  return render(request, template_name)

def profile(request):
  template_name = 'main/profile.html'
  return render(request, template_name)

def address(request):
  template_name = 'main/address.html'
  return render(request, template_name)

def orders(request):
  template_name = 'main/orders.html'
  return render(request, template_name)

def checkout(request):
  template_name = 'main/checkout.html'
  return render(request, template_name)

def mobile_category(request):
  template_name = 'main/mobile_category.html'
  return render(request, template_name)

def registration(request):
  template_name = 'main/registration.html'
  return render(request, template_name)

def login(request):
  template_name = 'main/login.html'
  return render(request, template_name)

def password_change(request):
  template_name = 'main/password_change.html'
  return render(request, template_name)

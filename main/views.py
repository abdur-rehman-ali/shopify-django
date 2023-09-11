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
  product = Product.objects.get(id=id)
  template_name = 'main/product_detail.html'
  context = { 'product': product }
  return render(request, template_name, context)

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

def mobile_category(request, data=None):
  if data is None:
    mobiles = Product.objects.filter(category='Mobile')
  elif data == 'apple' or data == 'samsung':
    mobiles = Product.objects.filter(category='Mobile').filter(brand=data)
  elif data == 'less_than_300':
    mobiles = Product.objects.filter(category='Mobile').filter(selling_price__lte=300)
  elif data == 'less_than_500':
    mobiles = Product.objects.filter(category='Mobile').filter(selling_price__lte=500)
  else:
    mobiles = Product.objects.filter(category='Mobile')
  template_name = 'main/mobile_category.html'
  context = {'mobiles': mobiles}
  return render(request, template_name, context)

def registration(request):
  template_name = 'main/registration.html'
  return render(request, template_name)

def login(request):
  template_name = 'main/login.html'
  return render(request, template_name)

def password_change(request):
  template_name = 'main/password_change.html'
  return render(request, template_name)

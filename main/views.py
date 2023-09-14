from django.shortcuts import render, redirect
from .models import Product
from .forms import CustomerRegistrationForm, CustomerLoginForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login as auth_login, authenticate

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
  mobiles = Product.objects.filter(category='Mobile')
  if data == 'apple' or data == 'samsung':
    mobiles = mobiles.filter(brand=data)
  elif data == 'less_than_300':
    mobiles = mobiles.filter(selling_price__lte=300)
  elif data == 'less_than_500':
    mobiles = mobiles.filter(selling_price__lte=500)
  template_name = 'main/mobile_category.html'
  context = {'mobiles': mobiles}
  return render(request, template_name, context)

def laptop_category(request, data=None):
  laptops = Product.objects.filter(category='Laptop')
  if data == 'Apple' or data == 'HP':
    laptops = laptops.filter(brand=data)
  elif data == 'less_than_500':
    laptops = laptops.filter(selling_price__lte=500)
  elif data == 'less_than_1000':
    laptops = laptops.filter(selling_price__lte=1000)
  template_name = 'main/laptop_category.html'
  context = {'laptops': laptops}
  return render(request, template_name, context)

def registration(request):
  if request.method == 'POST':
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Registration successful!!!")
      form = CustomerRegistrationForm(label_suffix='')
      return redirect(reverse('registration'))
  else: 
    form = CustomerRegistrationForm(label_suffix='')
  context = {'form': form}
  template_name = 'main/registration.html'
  return render(request, template_name, context)

def login(request):
  if request.method == 'POST':
    form = CustomerLoginForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        auth_login(request, user)
        return redirect(reverse('profile'))
      else:
        messages.error(request, "Invalid credentials !!!")
  else:
    form = CustomerLoginForm()
  context = {'form': form}
  template_name = 'main/login.html'
  return render(request, template_name, context)

def password_change(request):
  template_name = 'main/password_change.html'
  return render(request, template_name)

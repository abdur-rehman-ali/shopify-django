# Django Imports 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import (
  login as auth_login,
  authenticate,
  logout as auth_logout,
  update_session_auth_hash
)
from django.contrib.auth.decorators import login_required

# Local Imports 
from .models import (
  Product,
  Address
)
from .forms import (
  CustomerRegistrationForm, 
  CustomerLoginForm, 
  CustomerPasswordChangeForm,
  AddressForm
)

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

@login_required(login_url='login')
def profile(request):
  if request.method == 'POST':
    form = AddressForm(request.POST)
    if form.is_valid():
      new_address = Address(
        street=form.cleaned_data['street'],
        state=form.cleaned_data['state'],
        city=form.cleaned_data['city'],
        country=form.cleaned_data['country'],
        zip_code=form.cleaned_data['zip_code'],
        phone_number=form.cleaned_data['phone_number'],
        user=request.user
      )
      new_address.save()
      messages.success(request, 'Your adress is successfully added!')
      return redirect(reverse('address'))
  else:
    form = AddressForm(label_suffix='')
  context = {'form': form}
  template_name = 'main/profile.html'
  return render(request, template_name, context)

@login_required(login_url='login')
def address(request):
  user_addresses = request.user.addresses.all()
  context = {'user_addresses': user_addresses}
  template_name = 'main/address.html'
  return render(request, template_name, context)

@login_required(login_url='login')
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
      user = form.save()
      auth_login(request, user)
      messages.success(request, "Registration successful!!!")
      return redirect(reverse('profile'))
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
        messages.success(request, "Login successful!!!")
        return redirect(reverse('profile'))
      else:
        messages.error(request, "Invalid credentials !!!")
  else:
    form = CustomerLoginForm()
  context = {'form': form}
  template_name = 'main/login.html'
  return render(request, template_name, context)

def logout(request):
  auth_logout(request)
  return redirect(reverse('home'))

@login_required(login_url='login')
def password_change(request):
  if request.method == 'POST':
    form = CustomerPasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Your password is successfully updated!')
        return redirect(reverse('password_change'))
  else:
    form = CustomerPasswordChangeForm(request.user)
  template_name = 'main/password_change.html'
  context = {'form': form}
  return render(request, template_name, context)

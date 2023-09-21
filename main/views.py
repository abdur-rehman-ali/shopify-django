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
from django.http import JsonResponse

# Local Imports 
from .models import (
  Product,
  Address,
  ShoppingCart,
  Order
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

@login_required(login_url='login')
def shopping_cart(request):
  cart_items = request.user.cart_items.all()
  amount_without_shipping, amount_with_shipping, shipping = calulate_cart_amount(cart_items)
  context = {
    'cart_items': cart_items,
    'amount_without_shipping': amount_without_shipping,
    'amount_with_shipping': amount_with_shipping,
    'shipping': shipping
  }
  template_name = 'main/shopping_cart.html'
  return render(request, template_name, context)

def calulate_cart_amount(cart_items):
  amount_without_shipping = 0
  for item in cart_items:
    amount_without_shipping += (item.product.discounted_price * item.quantity)
  shipping = 7.0
  amount_with_shipping = amount_without_shipping + shipping
  return float(amount_without_shipping), float(amount_with_shipping), float(shipping)

@login_required(login_url='login')
def update_cart(request):
  product_id = request.GET.get('product_id')
  behaviour = request.GET.get('behaviour')
  is_record_deleted = False
  if product_id is not None:
    cart_record = ShoppingCart.objects.filter(product=product_id).first()
    if cart_record and behaviour == 'plus_quantity':
      cart_record.quantity += 1
      cart_record.save()
    elif cart_record and behaviour == 'minus_quantity':
      if cart_record.quantity == 1:
        cart_record.delete()
      else: 
        cart_record.quantity -= 1
        cart_record.save()
    elif behaviour == 'remove_item':
        cart_record.delete()
    cart_record_length = len(ShoppingCart.objects.filter(product=product_id))
    if cart_record_length == 0:
      is_record_deleted = True
  cart_items = request.user.cart_items.all()
  amount_without_shipping, amount_with_shipping, shipping = calulate_cart_amount(cart_items)
  data = {
    'amount_without_shipping': amount_without_shipping,
    'amount_with_shipping': amount_with_shipping,
    'shipping': shipping,
    'quantity': cart_record.quantity,
    'is_record_deleted': is_record_deleted
  }
  return JsonResponse(data)


@login_required(login_url='login')
def add_to_cart(request):
  if request.method == 'POST':
    product_id = request.POST['product_id']
    if product_id is not None:
      product = Product.objects.get(id=product_id)
      user = request.user
      cart_record, created = ShoppingCart.objects.get_or_create(
        product=product,
        user=user
      )
      if not created:
        cart_record.quantity += 1
        cart_record.save()
      messages.success(request, 'Product has been added to cart')
      return redirect(request.META.get('HTTP_REFERER', '/'))


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
  orders = request.user.orders.all()
  template_name = 'main/orders.html'
  context = {
    'orders': orders
  }
  return render(request, template_name, context)

@login_required(login_url='login')
def checkout(request):
  cart_items = request.user.cart_items.all()
  addresses = request.user.addresses.all()
  context = {
    'cart_items': cart_items,
    'addresses': addresses
  }
  template_name = 'main/checkout.html'
  return render(request, template_name, context)

@login_required(login_url='login')
def confirm_order(request):
  address_id = request.GET.get('address_id')
  address = Address.objects.get(id=address_id)
  user = request.user
  cart_items = user.cart_items.all()
  for item in cart_items:
    Order(user=user, product=item.product, quantity=item.quantity, address=address).save()
    item.delete()
  messages.success(request, "Order Placed successfully")
  return redirect(reverse('orders'))

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

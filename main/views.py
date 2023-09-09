from django.shortcuts import render

def index(request):
  template_name = 'main/index.html'
  return render(request, template_name)

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

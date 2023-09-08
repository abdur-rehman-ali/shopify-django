from django.shortcuts import render

def index(request):
  template_name = 'main/index.html'
  return render(request, template_name)

def product_detail(request, id):
  template_name = 'main/product_detail.html'
  image_url = f"main/images/product/{id}.jpg"
  content = {'id': id, 'image_url': image_url}
  return render(request, template_name, content)
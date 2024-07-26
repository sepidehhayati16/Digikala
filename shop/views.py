from django.shortcuts import render
from .models import Product

# Create your views here.
def hello(request):
    all_products = Product.objects.all()
    return render(request, 'index.html' , {'products': all_products})
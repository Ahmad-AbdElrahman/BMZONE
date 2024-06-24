from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def sproduct(request):
    return render(request, 'core/sproduct.html')

def contact(request):
    return render(request, 'core/contact.html')

def cart(request):
    return render(request, 'core/cart.html')

def shop(request):
    return render(request, 'core/shop.html')

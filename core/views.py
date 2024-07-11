from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from userauths.models import *
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'core/index.html', context)

def about(request):
    context = {}
    return render(request, 'core/about.html', context)

def sproduct(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'core/sproduct.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0}

    context = {'items':items, 'order':order}
    return render(request, 'core/checkout.html', context)

def contact(request):
    context = {}
    return render(request, 'core/contact.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0}

    context = {'items':items, 'order':order}
    return render(request, 'core/cart.html', context)

def shop(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'core/shop.html', context)

def updateItem(request):
    return JsonResponse('Item was added', safe=False)
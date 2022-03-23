from django.shortcuts import render
from django.http import HttpResponse
from . models import *

def main(request):
    context = {}
    return render (request, 'A_apps/main.html', context)

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'A_apps/store.html', context)

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}

    context = {'items':items, 'order':order}
    return render(request, 'A_apps/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}

    context = {'items':items, 'order':order}

    return render(request, 'A_apps/checkout.html', context)


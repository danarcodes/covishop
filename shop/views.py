import json
import datetime
from .models import *
from .utils import *
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# wenn Startseite aufgerufen wird


def landingpage(request):
    context = {}
    return render(request, 'shop/landingpage.html', context)


# wenn die Shop aufgerufen wird


def shop(request):
    data = cartData(request)

    cartItems = data['cartItems']
    # hier werden alle Produkte geladen
    products = Product.objects.all()
    # context übergibt an HTML
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'shop/shop.html', context)


# wenn der WK aufgerufen wird


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'shop/cart.html', context)

# wenn die Kasse aufgerufen wird


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'shop/checkout.html', context)

# checkout.html sendet nach erfolgreicher Zahlung, mit csrf-token, an diese view


@csrf_exempt
def processOrder(request):
    data = json.loads(request.body)
    getOrder(request, data)

    return JsonResponse('Bezahlung erfolgt', safe=False)

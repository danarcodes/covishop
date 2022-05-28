import datetime
import json
from .models import *

# hier wird der Cookie gelesen


def cookieCart(request):

    # wenn vorhanden, geladen
    try:
        cart = json.loads(request.COOKIES['cart'])
    # ansonsten neuer Cookie, wichtig da sonst Fehler auftauchen
    except:
        cart = {}
        print('Warenkorb:', cart)

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']

    for i in cart:
        # Cookie auslesen
        try:
            if(cart[i]['quantity'] > 0):  # items with negative quantity = lot of freebies
                cartItems += cart[i]['quantity']

                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quantity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                    'id': product.id,
                    'product': {'id': product.id, 'name': product.name, 'price': product.price,
                                'imageURL': product.imageURL}, 'quantity': cart[i]['quantity'],
                    'get_total': total,
                }
                items.append(item)
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items': items}

# Übergibt die WK Inhalt an die view


def cartData(request):
    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    order = cookieData['order']
    items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}

# Wenn die Bestellung abgeschlossen ist werden hier die Infos subtrahiert


def getOrder(request, data):
    cookieData = cookieCart(request)
    name = data['form']['name']
    email = data['form']['email']
    items = cookieData['items']

    # Wenn der Kunde vorhanden ist, wird kein neuer angelegt
    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    # Bestellung wird angelegt
    order = Order.objects.create(
        customer=customer,
        complete=True,
        transaction_id=datetime.datetime.now().timestamp()
    )
    order.save()

    # für jeden Artikel, eine OrderItem
    for item in items:
        product = Product.objects.get(id=item['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=(item['quantity'] if item['quantity']
                      > 0 else -1*item['quantity']),
        )

    address = ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['versand']['addresse'],
        city=data['versand']['stadt'],
        zipcode=data['versand']['plz'],
    )
    address.save()

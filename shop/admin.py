from django.contrib import admin
from .models import *

# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-options


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name',  'email']
    list_editable = ['email']
    list_per_page = 10
    ordering = ['name', 'email']
    search_fields = ['name__istartswith', 'email__istartswith']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',  'price',
                    'description', 'inventory', 'inventory_status']
    list_editable = ['price', 'description', 'inventory']
    list_per_page = 10
    ordering = ['name', 'price']
    search_fields = ['name__istartswith']

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer',  'date_ordered', 'complete']
    list_editable = ['complete']
    list_per_page = 10
    ordering = ['customer', 'date_ordered', 'complete']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product',  'order', 'quantity', 'date_added']
    list_per_page = 10
    ordering = ['order', 'date_added']


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer',  'address', 'city', 'zipcode']
    list_editable = ['address', 'city', 'zipcode']
    list_per_page = 10
    ordering = ['customer', 'city']

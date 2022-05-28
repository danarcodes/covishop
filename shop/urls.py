from django.urls import path

from . import views

urlpatterns = [
    # hier sind die URLs, '' ist für die Hauptseite
    path('', views.landingpage, name="landingpage"),
    path('shop/', views.shop, name="shop"),
    path('warenkorb/', views.cart, name="cart"),
    path('kasse/', views.checkout, name="checkout"),
    path('process_order/', views.processOrder, name="process_order"),

]

from django.urls import path
from .views import home, contact, about, shop, shop_single

# app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('shop', shop, name='shop'),
    path('shop/single', shop_single, name='shop_single'),

]

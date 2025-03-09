from django.urls import path
from .views import home, contact, about, shop

# app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about , name='about'),
    path('shop', shop, name='shop')

]

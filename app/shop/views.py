from django.shortcuts import render, get_object_or_404
from .models import Category, Product




def home(request):
    return render(request, 'shop/index.html')


def contact(request):
    return render(request, 'shop/contact.html')


def about(request):
    return render(request, 'shop/about.html')


def shop(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'shop/shop.html', context)

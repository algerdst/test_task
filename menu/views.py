from django.shortcuts import render
from .models import Menu


def index(request):
    return render(request, 'menu/index.html')


def menu(request, slug):
    data = {
        'slug': slug
    }
    return render(request, 'menu/menu.html', context=data)

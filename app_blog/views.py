import random
from datetime import datetime

from django.shortcuts import render


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Create your views here.


def starting_page(request):
    context = {
        'page_name': 'Main page'
    }

    return render(request, "index.html", context)


def time_page(request):
    context = {
        'page_name': 'Time page',
    }

    context['date'] = datetime.now().strftime('%y/%m/%d')
    context['time'] = datetime.now().strftime('%H:%M:%S')

    return render(request, "time.html", context)


def shop_page(request):
    context = {
        'page_name': 'Shop page',
    }

    item_name = ['Game#1', "Game#2", "Game#3", "Game#4"]

    items = [Item(name, random.randint(100, 2000)) for name in item_name]

    context['items'] = items

    return render(request, "forum_shop.html", context)

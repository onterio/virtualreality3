from django.shortcuts import render
from VRapp.models import Temes, Items

def index(request):
    return render(request, 'VRapp/index.html')


def catalog(request):
    categories = Temes.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }

    return render(request, 'VRapp/catalog.html', context)


def items(request, pk):
    itemes = Items.objects.filter(temes_id=pk)
    context = {
        'itemes': itemes,
        'page_title': 'страница'
    }

    return render(request, 'VRapp/items.html', context)

def items_page(request, items_pk):
    items = Items.objects.get(pk=items_pk)
    context = {
        'items': items,
        'page_title': 'страница '
    }
    return render(request, 'VRapp/items_page.html', context)
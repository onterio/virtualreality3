from basketapp.models import ItemsBasket
from VRapp.models import Items
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from django.urls import reverse



def index(request):
    items = ItemsBasket.objects.filter(user=request.user)
    context = {
        'object_list': items,
    }

    return render(request, 'basketapp/index.html', context)


def add(request, itemse_id):
    itemse = Items.objects.get(pk=itemse_id)
    ItemsBasket.objects.get_or_create(
        user=request.user,
        itemse=itemse
    )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, itemse_basket_id):
    if request.is_ajax():
        item = ItemsBasket.objects.get(id=itemse_basket_id)
        item.delete()
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return JsonResponse({'status': 'ok',
                             'itemse_basket_id': itemse_basket_id})
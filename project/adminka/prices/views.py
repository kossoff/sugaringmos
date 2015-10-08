# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from adminka.prices.models import PricePic, PriceText
from petrosugar.settings import os


# --- PRICE PAGE ----------------------------------------------------


def prices_page(request):
    """ Вывод страницы со списком вопросов и ответов """
    prices = []
    if PricePic.objects.all().count() > 0:
        prices = PricePic.objects.all()[0]
    if PriceText.objects.all().count() == 0:
        text = PriceText.objects.create()
        text.save()
    else:
        text = PriceText.objects.all()[0]
    return render(request, 'adminka_prices.html', {'prices': prices, 'text': text})


def prices_text(request, tid):
    """ Контроллер текста с ценами """
    PriceText.objects.filter(id=tid).update(text=request.REQUEST['prices_text'])
    return HttpResponseRedirect(reverse('ns_adminka:ns_prices:page'))


def prices_image(request):
    """ Контроллер картинки с ценами """
    if request.FILES.get('prices_image'):
        pricepics = PricePic.objects.all()
        if pricepics.count() > 0:
            for p in pricepics:
                thumb = p.image.path + "." + p.size + "_q85_crop-smart.jpg"
                if os.path.isfile(thumb):
                    os.remove(thumb)
                p.image.delete()
                p.delete()
        img_file = request.FILES['prices_image']
        pic = PricePic.objects.create()
        pic.save()
        pic.image = img_file
        pic.filename = img_file
        pic.save()
    return HttpResponseRedirect(reverse('ns_adminka:ns_prices:page'))
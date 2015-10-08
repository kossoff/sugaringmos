# -*- coding: utf8 -*-
from django.shortcuts import render
from adminka.frontpage.models import FrontpageSlide, FrontpageBanner, FrontpageAdvert
from adminka.prices.models import PricePic, PriceText
from adminka.sugarwaxing.models import PageType1
from adminka.services.models import Service, ServicePic
from adminka.faq.models import FAQRecord
from adminka.views import anonymous
from django.http import Http404


@anonymous
def frontpage(request):
    """ Вывод главной страницы """
    return render(request, 'frontend_frontpage.html', {'banner': FrontpageBanner.objects.all()[0],
                                                       'slides': FrontpageSlide.objects.filter(enabled=True),
                                                       'adverts': FrontpageAdvert.objects.filter(enabled=True)})


@anonymous
def price(request):
    """ Вывод страницы цены """
    return render(request, 'frontend_price.html', {'price': PricePic.objects.all()[0],
                                                   'text': PriceText.objects.all()[0]})


@anonymous
def faq(request):
    """ Вывод страницы вопросы и ответы """
    return render(request, 'frontend_faq.html', {'faq': FAQRecord.objects.filter(enabled=True)})


@anonymous
def sugarwaxing(request):
    """ Вывод страницы шугаринг или воск """
    return render(request, 'frontend_sugarwaxing.html', {'pg': PageType1.objects.get(section=u'sugarwaxing')})


@anonymous
def contacts(request):
    """ Вывод страницы контактов """
    return render(request, 'frontend_contacts.html')


@anonymous
def service(request, service_link):
    """ Вывод страницы услуги """
    if Service.objects.filter(link=service_link).count() > 0:
        serv = Service.objects.get(link=service_link)
        pics = ServicePic.objects.filter(service=serv)
    else:
        raise Http404
    return render(request, 'frontend_service.html', {'service': serv, 'pics': pics})
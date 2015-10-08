# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from adminka.contacts.models import Contact
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def fill_contacts():
    """ Заполнение таблицы контактов базовыми записями """
    Contact.objects.bulk_create([
        Contact(code=u'phone', name=u'Телефон', body=u'8 (888) 888-8888'),
        Contact(code=u'email', name=u'E-mail', body=u'test@heaven.god'),
        Contact(code=u'brand', name=u'Название компании', body=u'ОАО "Рога и копыта"'),
        Contact(code=u'address', name=u'Адрес', body=u'123456, Москва, ул. Штирлица, д.11'),
        Contact(code=u'weekdays', name=u'Пн. - Пт.', body=u'9:00 - 21:00'),
        Contact(code=u'weekend', name=u'Сб. - Вс.', body=u'10:00 - 18:00'),
        Contact(code=u'map', name=u'Карта', body=u'MAP_SCRIPT'),
        Contact(code=u'text', name=u'Текст', body=u'DEFAULT_TEXT')
    ])
    return False


# --- CONTACTS ------------------------------------------------------


def contacts_list(request):
    """ Вывод страницы со списком контактных данных """
    if Contact.objects.all().count() == 0:
        fill_contacts()
    return render(request, 'contacts/adminka_contacts_list.html', {'conlist': Contact.objects.all()})


def contacts_edit(request):
    """ Вывод страницы с редактирование контактных данных """
    return render(request, 'contacts/adminka_contacts_edit.html', {'conlist': Contact.objects.all()})


def contacts_update(request):
    """ UPDATE-контроллер для контактнвых данных """
    Contact.objects.filter(code=u'phone').update(body=request.REQUEST['con_phone'])
    Contact.objects.filter(code=u'email').update(body=request.REQUEST['con_email'])
    Contact.objects.filter(code=u'brand').update(body=request.REQUEST['con_brand'])
    Contact.objects.filter(code=u'address').update(body=request.REQUEST['con_address'])
    Contact.objects.filter(code=u'weekdays').update(body=request.REQUEST['con_weekdays'])
    Contact.objects.filter(code=u'weekend').update(body=request.REQUEST['con_weekend'])
    Contact.objects.filter(code=u'map').update(body=request.REQUEST['con_map'])
    Contact.objects.filter(code=u'text').update(body=request.REQUEST['con_text'])
    return HttpResponseRedirect(reverse('ns_adminka:ns_contacts:list'))
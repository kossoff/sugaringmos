# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from adminka.services.models import Service, ServicePic
from petrosugar.translit import transliterate
from petrosugar.settings import os


# --- SERVICES PAGE -------------------------------------------------


def service_list(request):
    """ Вывод страницы со списком услуг """
    return render(request, 'services/adminka_service_list.html', {'services': Service.objects.all()})


def service_single(request, sid):
    """ Вывод страницы с данными отдельной услуги """
    serv = Service.objects.get(id=sid)
    return render(request, 'services/adminka_service_single.html',
                  {'service': serv,
                   'pics': ServicePic.objects.filter(service=serv)})


def service_active(request, sid, action_type):
    """ Контроллер изменения видимости страниц услуг """
    if action_type == 'enable':
        Service.objects.filter(id=sid).update(enabled=True)
    elif action_type == 'disable':
        Service.objects.filter(id=sid).update(enabled=False)
    return HttpResponseRedirect(reverse('ns_adminka:ns_services:single', args=[str(sid)]))


def service_crud(request, sid, action_type):
    """ CRUD-контроллер услуг """
    if action_type == 'insert':
        service = Service()
        service.save()
        sid = service.id
    elif action_type == 'delete':
        Service.objects.filter(id=sid).delete()
        return HttpResponseRedirect(reverse('ns_adminka:ns_services:list'))
    elif action_type == 'update':
        Service.objects.filter(id=sid).update(title=request.REQUEST['service_title'],
                                              link=transliterate(request.REQUEST['service_title']),
                                              text=request.REQUEST['service_text'])
    return HttpResponseRedirect(reverse('ns_adminka:ns_services:single', args=[str(sid)]))


def service_image(request, sid, picid, action_type):
    """ Контроллер картинок услуг """
    serv = Service.objects.get(id=sid)
    if action_type == 'insert':
        if request.FILES.get('service_image'):
            pic = ServicePic.objects.create(image=request.FILES['service_image'],
                                            filename=request.FILES['service_image'],
                                            position=ServicePic.objects.filter(service=serv).count() + 1,
                                            service=serv)
            pic.save()
    elif action_type == 'delete':
        pic = ServicePic.objects.get(id=picid)
        thumb = pic.image.path + "." + "170x120" + "_q85_crop-smart.jpg"
        if os.path.isfile(thumb):
            os.remove(thumb)
        pic.image.delete()
        ServicePic.objects.filter(id=picid).delete()
    elif action_type == 'posinc' or action_type == 'posdec':
        picthis = ServicePic.objects.get(id=picid)
        pos = picthis.position
        if action_type == 'posinc':
            picnext = ServicePic.objects.get(position=pos+1)
            picthis.position = pos+1
            picnext.position = pos
            picthis.save()
            picnext.save()
        elif action_type == 'posdec':
            picprev = ServicePic.objects.get(position=pos-1)
            picthis.position = pos-1
            picprev.position = pos
            picthis.save()
            picprev.save()
    return HttpResponseRedirect(reverse('ns_adminka:ns_services:single', args=[str(sid)]))
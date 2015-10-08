# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from adminka.sugarwaxing.models import PageType1
from petrosugar.settings import os


# -------------------------------------------------------------------


def sugarwaxing_page(request):
    """ Вывод страницы Шугаринг или воск """
    if PageType1.objects.filter(section=u'sugarwaxing').count() == 0:
        pg = PageType1.objects.create(section=u'sugarwaxing')
        pg.save()
    else:
        pg = PageType1.objects.get(section=u'sugarwaxing')
    return render(request, 'adminka_sugarwaxing_single.html', {'pg': pg})


def sugarwaxing_edit(request, pid):
    """ Вывод страницы редактирования Шугаринг или Воск """
    return render(request, 'adminka_sugarwaxing_edit.html', {'pg': PageType1.objects.get(id=pid)})


def sugarwaxing_crud(request, pid, action_type):
    """ CRUD-контроллер вопросов и ответов """
    if action_type == 'update':
        PageType1.objects.filter(id=pid).update(text=request.REQUEST['sugarwaxing_text'])
    return HttpResponseRedirect(reverse('ns_adminka:ns_sugarwaxing:page'))


def sugarwaxing_image(request, pid, action_type):
    """ Контроллер картинок """
    pg = PageType1.objects.get(id=pid)
    if action_type == 'upload':
        if request.FILES.get('faq_image'):
            if pg.image:
                thumb = pg.image.path + "." + "819x614" + "_q85_crop-smart.jpg"
                if os.path.isfile(thumb):
                    os.remove(thumb)
                pg.image.delete()
            img_file = request.FILES['faq_image']
            pg.image = img_file
            pg.filename = img_file
    elif action_type == 'clear':
        thumb = pg.image.path + "." + "819x614" + "_q85_crop-smart.jpg"
        if os.path.isfile(thumb):
            os.remove(thumb)
        pg.image.delete()
        pg.filename = None
        pg.size = u'170x120'
    pg.save()
    return HttpResponseRedirect(reverse('ns_adminka:ns_sugarwaxing:page'))
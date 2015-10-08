# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from adminka.faq.models import FAQRecord
from petrosugar.settings import os
from datetime import datetime


# --- FAQ -----------------------------------------------------------


def faq_list(request):
    """ Вывод страницы со списком вопросов и ответов"""
    return render(request, 'faq/adminka_faq_list.html', {'faq_list': FAQRecord.objects.all()})


def faq_new(request):
    """ Вывод страницы с формой добавления нового вопроса-ответа """
    return render(request, 'faq/adminka_faq_new.html')


def faq_edit(request, fid):
    """ Вывод страницы редактирования отдельного вопроса-ответа """
    return render(request, 'faq/adminka_faq_edit.html', {'faq': FAQRecord.objects.get(id=fid)})


def faq_single(request, fid):
    """ Вывод страницы с данными отдельного вопроса-ответа """
    return render(request, 'faq/adminka_faq_single.html', {'faq': FAQRecord.objects.get(id=fid)})


def faq_crud(request, fid, action_type):
    """ CRUD-контроллер вопросов и ответов """
    if action_type == 'insert':
        faq = FAQRecord(question=request.REQUEST['faq_question'],
                        answer=request.REQUEST['faq_answer'])
        faq.position = FAQRecord.objects.all().count() + 1
        faq.save()
        fid = faq.id
    elif action_type == 'delete':
        FAQRecord.objects.filter(id=fid).delete()
        return HttpResponseRedirect(reverse('ns_adminka:ns_faq:list'))
    elif action_type == 'update':
        # UPDATE не вызывает метод save(), т.е. auto_now=True для поля changed не сработает!!!
        FAQRecord.objects.filter(id=fid).update(question=request.REQUEST['faq_question'],
                                                answer=request.REQUEST['faq_answer'],
                                                changed=datetime.now())
    return HttpResponseRedirect(reverse('ns_adminka:ns_faq:single', args=[str(fid)]))


def faq_position(request, fid, action_type):
    """ Контроллер изменения порядка вопросов и ответов """
    faqthis = FAQRecord.objects.get(id=fid)
    pos = faqthis.position
    if action_type == 'posinc':
        faqnext = FAQRecord.objects.get(position=pos+1)
        faqthis.position = pos+1
        faqnext.position = pos
        faqthis.save()
        faqnext.save()
    elif action_type == 'posdec':
        faqprev = FAQRecord.objects.get(position=pos-1)
        faqthis.position = pos-1
        faqprev.position = pos
        faqthis.save()
        faqprev.save()
    return HttpResponseRedirect(reverse('ns_adminka:ns_faq:list'))


def faq_active(request, fid, action_type):
    """ Контроллер изменения видимости вопросов и ответов """
    if action_type == 'enable':
        FAQRecord.objects.filter(id=fid).update(enabled=True)
    elif action_type == 'disable':
        FAQRecord.objects.filter(id=fid).update(enabled=False)
    return HttpResponseRedirect(reverse('ns_adminka:ns_faq:single', args=[str(fid)]))


def faq_image(request, fid, action_type):
    """ Контроллер картинок вопросов и ответов """
    faq = FAQRecord.objects.get(id=fid)
    if action_type == 'upload':
        if request.FILES.get('faq_image'):
            if faq.image:
                thumb = faq.image.path + "." + faq.size + "_q85_crop-smart.jpg"
                if os.path.isfile(thumb):
                    os.remove(thumb)
                faq.image.delete()
            img_file = request.FILES['faq_image']
            faq.image = img_file
            faq.filename = img_file
        if request.REQUEST.get('faq_size'):
            old = faq.image.path + "." + faq.size + "_q85_crop-smart.jpg"
            if os.path.isfile(old):
                os.remove(old)
            faq.size = request.REQUEST['faq_size']
    elif action_type == 'clear':
        thumb = faq.image.path + "." + faq.size + "_q85_crop-smart.jpg"
        if os.path.isfile(thumb):
            os.remove(thumb)
        faq.image.delete()
        faq.filename = None
        faq.size = u'170x120'
    elif action_type == 'align_left':
        faq.align_left = True
    elif action_type == 'align_right':
        faq.align_left = False
    faq.save()
    return HttpResponseRedirect(reverse('ns_adminka:ns_faq:single', args=[str(fid)]))
# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from adminka.frontpage.models import FrontpageSlide, FrontpageBanner, FrontpageAdvert
from petrosugar.settings import os


# --- FRONTPAGE -----------------------------------------------------


def frontpage_home(request):
    """ Вывод главной страницы """
    if FrontpageBanner.objects.all().count() == 0:
        banner = FrontpageBanner.objects.create()
        banner.save()
    else:
        banner = FrontpageBanner.objects.all()[0]
    return render(request, 'frontpage/adminka_frontpage_list.html', {'banner': banner,
                                                                     'slides': FrontpageSlide.objects.all(),
                                                                     'adverts': FrontpageAdvert.objects.all()})


# --- FRONTPAGE SLIDER ----------------------------------------------


def frontpage_slide_single(request, sid):
    """ Вывод страницы с данными отдельного слайда """
    return render(request, 'frontpage/adminka_frontpage_slide_single.html',
                  {'slide': FrontpageSlide.objects.get(id=sid)})


def frontpage_slide_crud(request, sid, action_type):
    """ CRUD-контроллер слайдов """
    if action_type == 'insert':
        slide = FrontpageSlide()
        slide.position = FrontpageSlide.objects.all().count() + 1
        slide.save()
        sid = slide.id
    elif action_type == 'delete':
        slide = FrontpageSlide.objects.get(id=sid)
        if slide.image:
            thumb = slide.image.path + "." + "170x120" + "_q85_crop-smart.jpg"
            if os.path.isfile(thumb):
                os.remove(thumb)
            slide.image.delete()
        FrontpageSlide.objects.filter(id=sid).delete()
        return HttpResponseRedirect(reverse('ns_adminka:ns_frontpage:list'))
    elif action_type == 'update':
        # UPDATE не вызывает метод save(), т.е. auto_now=True для поля changed не сработает!!!
        slide = FrontpageSlide.objects.get(id=sid)
        if request.REQUEST.get('slide_title'):
            slide.title = request.REQUEST['slide_title']
        if request.FILES.get('slide_image'):
            if slide.image:
                thumb = slide.image.path + "." + "170x120" + "_q85_crop-smart.jpg"
                if os.path.isfile(thumb):
                    os.remove(thumb)
                slide.image.delete()
            img_file = request.FILES['slide_image']
            slide.image = img_file
            slide.filename = img_file
        slide.save()
    elif action_type == 'clear':
        slide = FrontpageSlide.objects.get(id=sid)
        thumb = slide.image.path + "." + "170x120" + "_q85_crop-smart.jpg"
        if os.path.isfile(thumb):
            os.remove(thumb)
        slide.image.delete()
        slide.filename = None
        slide.save()
    elif action_type == 'posinc' or action_type == 'posdec':
        slidethis = FrontpageSlide.objects.get(id=sid)
        pos = slidethis.position
        if action_type == 'posinc':
            slidenext = FrontpageSlide.objects.get(position=pos+1)
            slidethis.position = pos+1
            slidenext.position = pos
            slidethis.save()
            slidenext.save()
        elif action_type == 'posdec':
            slideprev = FrontpageSlide.objects.get(position=pos-1)
            slidethis.position = pos-1
            slideprev.position = pos
            slidethis.save()
            slideprev.save()
        return HttpResponseRedirect(reverse('ns_adminka:ns_frontpage:list'))
    return HttpResponseRedirect(reverse('ns_adminka:ns_frontpage:slide_single', args=[str(sid)]))


def frontpage_slide_active(request, sid, action_type):
    """ Контроллер изменения видимости слайдов """
    if action_type == 'enable':
        FrontpageSlide.objects.filter(id=sid).update(enabled=True)
    elif action_type == 'disable':
        FrontpageSlide.objects.filter(id=sid).update(enabled=False)
    return HttpResponseRedirect(reverse('ns_adminka:ns_frontpage:slide_single', args=[str(sid)]))


# --- FRONTPAGE BANNER ----------------------------------------------


def frontpage_banner(request, bid, action_type):
    """ Контроллер баннера """
    banner = FrontpageBanner.objects.get(id=bid)
    if action_type == 'upload':
        if request.FILES.get('banner_image'):
            if banner.image:
                thumb = banner.image.path + "." + "1400x320" + "_q85_crop-smart.jpg"
                if os.path.isfile(thumb):
                    os.remove(thumb)
                banner.image.delete()
            img_file = request.FILES['banner_image']
            banner.image = img_file
            banner.filename = img_file
    elif action_type == 'clear':
        thumb = banner.image.path + "." + "1400x320" + "_q85_crop-smart.jpg"
        if os.path.isfile(thumb):
            os.remove(thumb)
        banner.image.delete()
        banner.filename = None
        banner.size = u'170x120'
    banner.save()
    return HttpResponseRedirect(reverse('ns_adminka:ns_frontpage:list'))


# --- FRONTPAGE ADVERT ----------------------------------------------


def frontpage_advert_single(request, advid):
    """ Вывод страницы с данными отдельного слайда """
    return render(request, 'frontpage/adminka_frontpage_advert_single.html',
                  {'advert': FrontpageAdvert.objects.get(id=advid)})


def frontpage_advert_crud(request, advid, action_type):
    """ CRUD-контроллер популярного """
    if action_type == 'insert':
        advert = FrontpageAdvert()
        advert.position = FrontpageAdvert.objects.all().count() + 1
        advert.save()
        advid = advert.id
    elif action_type == 'delete':
        advert = FrontpageAdvert.objects.get(id=advid)
        if advert.image:
            thumb = advert.image.path + "." + "240x240" + "_q85_crop-smart.jpg"
            if os.path.isfile(thumb):
                os.remove(thumb)
            advert.image.delete()
        FrontpageAdvert.objects.filter(id=advid).delete()
        return HttpResponseRedirect(reverse('ns_adminka:ns_frontpage:list'))
    elif action_type == 'update':
        # UPDATE не вызывает метод save(), т.е. auto_now=True для поля changed не сработает!!!
        advert = FrontpageAdvert.objects.get(id=advid)
        if request.REQUEST.get('advert_title'):
            advert.title = request.REQUEST['advert_title']
        if request.REQUEST.get('advert_link'):
            advert.link = request.REQUEST['advert_link']
        if request.REQUEST.get('advert_text'):
            advert.text = request.REQUEST['advert_text']
        if request.FILES.get('advert_image'):
            if advert.image:
                thumb = advert.image.path + "." + "240x240" + "_q85_crop-smart.jpg"
                if os.path.isfile(thumb):
                    os.remove(thumb)
                advert.image.delete()
            img_file = request.FILES['advert_image']
            advert.image = img_file
            advert.filename = img_file
        advert.save()
    elif action_type == 'clear':
        advert = FrontpageAdvert.objects.get(id=advid)
        thumb = advert.image.path + "." + "240x240" + "_q85_crop-smart.jpg"
        if os.path.isfile(thumb):
            os.remove(thumb)
        advert.image.delete()
        advert.filename = None
        advert.save()
    elif action_type == 'posinc' or action_type == 'posdec':
        advthis = FrontpageAdvert.objects.get(id=advid)
        pos = advthis.position
        if action_type == 'posinc':
            advnext = FrontpageSlide.objects.get(position=pos+1)
            advthis.position = pos+1
            advnext.position = pos
            advthis.save()
            advnext.save()
        elif action_type == 'posdec':
            advprev = FrontpageAdvert.objects.get(position=pos-1)
            advthis.position = pos-1
            advprev.position = pos
            advthis.save()
            advprev.save()
        return HttpResponseRedirect(reverse('ns_adminka:ns_frontpage:list'))
    return HttpResponseRedirect(reverse('ns_adminka:ns_frontpage:advert_single', args=[str(advid)]))


def frontpage_advert_active(request, advid, action_type):
    """ Контроллер изменения видимости слайдов """
    if action_type == 'enable':
        FrontpageAdvert.objects.filter(id=advid).update(enabled=True)
    elif action_type == 'disable':
        FrontpageAdvert.objects.filter(id=advid).update(enabled=False)
    return HttpResponseRedirect(reverse('ns_adminka:ns_frontpage:advert_single', args=[str(advid)]))
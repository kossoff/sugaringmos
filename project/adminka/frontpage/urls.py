# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.frontpage_home, name='list'),
    url(r'^(?P<bid>\d+)/(?P<action_type>upload|clear)/$', views.frontpage_banner, name='banner'),
    url(r'^slide_(?P<sid>\d+)/$', views.frontpage_slide_single, name='slide_single'),
    url(r'^slide_(?P<sid>\d+)/(?P<action_type>enable|disable)/$', views.frontpage_slide_active, name='slide_active'),
    url(r'^slide_(?P<sid>\d+)/(?P<action_type>insert|update|delete|clear|posinc|posdec)/$',
        views.frontpage_slide_crud, name='slide_crud'),
    url(r'^advert_(?P<advid>\d+)/$', views.frontpage_advert_single, name='advert_single'),
    url(r'^advert_(?P<advid>\d+)/(?P<action_type>enable|disable)/$',
        views.frontpage_advert_active, name='advert_active'),
    url(r'^advert_(?P<advid>\d+)/(?P<action_type>insert|update|delete|clear|posinc|posdec)/$',
        views.frontpage_advert_crud, name='advert_crud'),
)

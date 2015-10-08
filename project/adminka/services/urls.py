# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.service_list, name='list'),
    url(r'^(?P<sid>\d+)/$', views.service_single, name='single'),
    url(r'^(?P<sid>\d+)/(?P<action_type>enable|disable)/$', views.service_active, name='active'),
    url(r'^(?P<sid>\d+)/(?P<action_type>insert|update|delete|clear|posinc|posdec)/$',
        views.service_crud, name='crud'),
    url(r'^(?P<sid>\d+)_image(?P<picid>\d+)/(?P<action_type>insert|delete|posinc|posdec)/$',
        views.service_image, name='image'),
)

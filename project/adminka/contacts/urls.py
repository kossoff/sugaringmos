# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.contacts_list, name='list'),
    url(r'^edit/$', views.contacts_edit, name='edit'),
    url(r'^update/$', views.contacts_update, name='update'),
)

# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.prices_page, name='page'),
    url(r'^change/$', views.prices_image, name='change'),
    url(r'^change_(?P<tid>\d+)/$', views.prices_text, name='change_text'),
    #url(r'^(?P<fid>\d+)/edit/$', views.faq_edit, name='edit'),
    #url(r'^(?P<fid>\d+)/(?P<action_type>upload|clear|align_left|align_right)/$', views.faq_image, name='image'),
    #url(r'^(?P<fid>\d+)/(?P<action_type>posinc|posdec)/$', views.faq_position, name='position'),
    #url(r'^(?P<fid>\d+)/(?P<action_type>enable|disable)/$', views.faq_active, name='active'),
    #url(r'^(?P<fid>\d+)/(?P<action_type>insert|update|delete)/$', views.faq_crud, name='crud'),

)

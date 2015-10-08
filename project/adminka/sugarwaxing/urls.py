# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.sugarwaxing_page, name='page'),
    #url(r'^image/$', views.sugarwaxing_image, name='image'),
    #url(r'^(?P<fid>\d+)/$', views.faq_single, name='single'),
    url(r'^(?P<pid>\d+)/edit/$', views.sugarwaxing_edit, name='edit'),
    url(r'^(?P<pid>\d+)/(?P<action_type>upload|clear)/$', views.sugarwaxing_image, name='image'),
    #url(r'^(?P<fid>\d+)/(?P<action_type>posinc|posdec)/$', views.faq_position, name='position'),
    #url(r'^(?P<fid>\d+)/(?P<action_type>enable|disable)/$', views.faq_active, name='active'),
    url(r'^(?P<pid>\d+)/(?P<action_type>update)/$', views.sugarwaxing_crud, name='crud'),

)

# -*- coding: utf8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

import views
import faq.urls
import prices.urls
import contacts.urls
import services.urls
import frontpage.urls
import frontpage.views
import sugarwaxing.urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    #url(r'^$', frontpage.views.frontpage_home, name='adhome'),
    url(r'^$', views.login_gate, name='adhome'),
    url(r'^login/$', views.gk_login, name='login'),
    url(r'^logout/$', views.gk_logout, name='logout'),
    url(r'^faq/', include(faq.urls, namespace='ns_faq')),
    url(r'^prices/', include(prices.urls, namespace='ns_prices')),
    url(r'^contacts/', include(contacts.urls, namespace='ns_contacts')),
    url(r'^services/', include(services.urls, namespace='ns_services')),
    url(r'^frontpage/', include(frontpage.urls, namespace='ns_frontpage')),
    url(r'^sugarwaxing/', include(sugarwaxing.urls, namespace='ns_sugarwaxing')),
    url(r'^changepass/$', views.changepass, name='changepass'),
    url(r'^changepass/new$', views.set_new_pwd, name='set_new_pwd'),
)

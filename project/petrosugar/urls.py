# -*- coding: utf8 -*-
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

#import dashboard.views
import adminka.frontpage.views
import adminka.urls
import front.views

admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^$', front.views.frontpage, name='home'),
    url(r'^faq/$', front.views.faq, name='faq'),
    url(r'^price/$', front.views.price, name='price'),
    url(r'^sugarwaxing/$', front.views.sugarwaxing, name='sugarwaxing'),
    url(r'^contacts/$', front.views.contacts, name='contacts'),
    url(r'^adminka/', include(adminka.urls, namespace='ns_adminka')),
    #url(r'^myenterprise', gatekeeper.views.myenterprise, name='myenterprise'),
    #url(r'^enterprise/', include(enterprise.urls, namespace='ns_enterprise')),
    #url(r'^fieldtypes/', include(fieldtype.urls, namespace='ns_fieldtype')),
    #url(r'^fields/', include(field.urls, namespace='ns_field')),
    #url(r'^payments/', include(payments.urls, namespace='ns_payments')),
    #url(r'^login_gate/$', frontpage.urls.login_gate, name='login_gate'),
    #url(r'^table1/', include(frontpage.urls, namespace='ns_table1')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    url(r'^(?P<service_link>.*)/$', front.views.service, name='service'),
)

urlpatterns += staticfiles_urlpatterns()
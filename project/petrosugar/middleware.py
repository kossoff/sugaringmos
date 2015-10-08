# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect


class FullAuthMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if not getattr(view_func, 'anonymous', False):
            if request.user.is_authenticated():
                return None
            return HttpResponseRedirect('/')
        return None
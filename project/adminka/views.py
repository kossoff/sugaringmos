# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render


# --- SERVICE FUNCTIONS --------------------------------------------


def anonymous(view):
    view.anonymous = True
    return view


# --- ENTERPRISE ----------------------------------------------------


@anonymous
def login_gate(request):
    """Вывод страницы для входа в систему"""
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('ns_adminka:ns_frontpage:list'))
    return render(request, 'adminka_login.html')

@anonymous
def gk_login(request):
    """Вход в систему"""
    if ('log' in request.REQUEST) and ('pwd' in request.REQUEST):
        log = request.REQUEST['log']
        pwd = request.REQUEST['pwd']
        user = authenticate(username=log, password=pwd)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/adminka/')
    return HttpResponseRedirect('/')


def gk_logout(request):
    """Выход из системы"""
    logout(request)
    return HttpResponseRedirect('/')


def changepass(request):
    """ Вывод страницы смены пароля """
    return render(request, 'adminka_changepass.html')


def set_new_pwd(request):
    """ Смена пароля """
    user = User.objects.get(is_superuser=True)
    user.set_password(request.REQUEST['new_pwd'])
    user.save()
    return render(request, 'adminka_changepass.html')
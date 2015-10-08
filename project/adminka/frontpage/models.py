# -*- coding: utf8 -*-
from django.db import models
from petrosugar.settings import os
from petrosugar.translit import transliterate


# --- HOME SLIDER ---------------------------------------------------


def get_slide_path(instance, filename):
    """ Функция get_slide_path предназначена для определения
    пути загрузки изображений для слайдов элемента 'слайдер' """
    return os.path.join('frontpage_slides', str(instance.id) + "_" + transliterate(filename))


class FrontpageSlide(models.Model):
    """ Модель данных HomepageSlide предназначена
    для хранения слайдов элемента 'слайдер' главной страницы
    ------------------------------------------
    title - название слайда (выводится как хештег в слайдере)
    image - путь до файла в файловой системе
    filename - название файла с расширением
    block - внешний ключ на блок главной страницы
    ------------------------------------------
    Таблица в БД: frontpage_slides """
    title = models.CharField(max_length=20, blank=True, null=True)
    image = models.FileField(upload_to=get_slide_path, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    enabled = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']
        db_table = u'frontpage_slides'


# --- HOME BANNER ---------------------------------------------------


def get_banner_path(instance, filename):
    """ Функция get_banner_path предназначена для определения
    пути загрузки изображений для баннеров на главной странице """
    return os.path.join('frontpage_banners', str(instance.id), transliterate(filename))


class FrontpageBanner(models.Model):
    """ Модель данных HomepageBanner предназначена
    для хранения полноразмерных баннеров главной страницы
    ------------------------------------------
    image - путь до файла в файловой системе
    filename - название файла с расширением
    block - внешний ключ на блок главной страницы
    ------------------------------------------
    Таблица в БД: frontpage_banners """
    image = models.FileField(upload_to=get_banner_path, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)

    class Meta:
        db_table = u'frontpage_banners'


# --- HOME ADVERT ---------------------------------------------------


def get_advert_path(instance, filename):
    """ Функция get_advert_path предназначена для определения
    пути загрузки изображений для блоков с услугами на главной странице """
    return os.path.join('frontpage_adv', str(instance.id) + "_" + transliterate(filename))


class FrontpageAdvert(models.Model):
    """ Модель данных HomepageAdvert предназначена
    для хранения блоков услуг главной страницы
    ------------------------------------------
    title - заголовок
    link - ссылка на другую страницу
    text - основной текст
    image - путь до файла в файловой системе
    filename - название файла с расширением
    block - внешний ключ на блок главной страницы
    ------------------------------------------
    Таблица в БД: frontpage_advert """
    title = models.CharField(max_length=30)
    link = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    image = models.FileField(upload_to=get_advert_path, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    enabled = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']
        db_table = u'frontpage_advert'
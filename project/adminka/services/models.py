# -*- coding: utf8 -*-
from django.db import models
from petrosugar.settings import os
from petrosugar.translit import transliterate


# --- SERVICE PAGE --------------------------------------------------


class Service(models.Model):
    """ Модель данных Service предназначена
    для страниц в разделе УСЛУГИ
    --------------------------------------------------------
    title - название страницы
    link - чистая ссылка страницы
    text - текст страницы
    has_gallery - содержит ли страница несколько изображений
    --------------------------------------------------------
    Таблица в БД: services """
    title = models.CharField(max_length=250, blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    enabled = models.BooleanField(default=False)
    has_gallery = models.BooleanField(default=False)

    class Meta:
        db_table = u'services'


def get_service_pic_path(instance, filename):
    """ Функция get_service_pic_path предназначена для определения
    пути загрузки изображений для раздела УСЛУГИ """
    return os.path.join('service_pics', str(instance.service.id), transliterate(filename))


class ServicePic(models.Model):
    """ Модель данных ServicePic предназначена
    для изображения в разделе УСЛУГИ
    ------------------------------------------
    image - путь до файла в файловой системе
    filename - название файла с расширением
    position - порядок вывода картинок
    ------------------------------------------
    Таблица в БД: service_pics """
    image = models.FileField(upload_to=get_service_pic_path, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    position = models.IntegerField(default=0)
    service = models.ForeignKey(Service)

    class Meta:
        ordering = ['position']
        db_table = u'service_pics'
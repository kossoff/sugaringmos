# -*- coding: utf8 -*-
from django.db import models
from petrosugar.settings import os
from petrosugar.translit import transliterate


# --- HOME SLIDER ---------------------------------------------------


def get_pagetype1pic_path(instance, filename):
    """ Функция get_pagetype1pic_path предназначена для определения
    пути загрузки изображений для страниц """
    return os.path.join('pagepics', str(instance.id) + "_" + transliterate(filename))


class PageType1(models.Model):
    """ Модель данных PageType1 предназначена
    для страницы Шугаринг vs. Воск
    ------------------------------------------
    text - текст страницы
    section - раздел, где находится страница
    image - путь до файла в файловой системе
    filename - название файла с расширением
    ------------------------------------------
    Таблица в БД: pages_type_1 """
    text = models.TextField(blank=True, null=True)
    section = models.CharField(max_length=20, default=u'default')
    image = models.FileField(upload_to=get_pagetype1pic_path, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = u'pages_type_1'
# -*- coding: utf8 -*-
from django.db import models
from petrosugar.settings import os
from petrosugar.translit import transliterate


# --- PRICE PAGE ----------------------------------------------------


def get_pricepic_path(instance, filename):
    """ Функция get_pricepic_path предназначена для определения
    пути загрузки изображений для раздела ВОПРОСЫ И ОТВЕТЫ """
    return os.path.join('pricepic', str(instance.id) + "_" + transliterate(filename))


class PricePic(models.Model):
    """ Модель данных PricePic предназначена
    для изображения в разделе ЦЕНЫ
    ------------------------------------------
    image - путь до файла в файловой системе
    filename - название файла с расширением
    size - разрешение миниатюры изображения
    ------------------------------------------
    Таблица в БД: price_pic """
    image = models.FileField(upload_to=get_pricepic_path, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    size = models.CharField(max_length=10, default=u'854x601')

    class Meta:
        db_table = u'price_pic'


class PriceText(models.Model):
    """ Модель данных PriceText предназначена
    для текста в разделе ЦЕНЫ
    ------------------------------------------
    image - путь до файла в файловой системе
    filename - название файла с расширением
    size - разрешение миниатюры изображения
    ------------------------------------------
    Таблица в БД: price_pic """
    text = models.TextField(blank=True, null=True)

    class Meta:
        db_table = u'price_text'
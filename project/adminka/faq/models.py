# -*- coding: utf8 -*-
from django.db import models
from petrosugar.settings import os
from petrosugar.translit import transliterate


# --- HOME SLIDER ---------------------------------------------------


def get_faqpic_path(instance, filename):
    """ Функция get_faqpic_path предназначена для определения
    пути загрузки изображений для раздела ВОПРОСЫ И ОТВЕТЫ """
    return os.path.join('faqpics', str(instance.id) + "_" + transliterate(filename))


class FAQRecord(models.Model):
    """ Модель данных FAQRecord предназначена
    для записей раздела ВОПРОСЫ И ОТВЕТЫ
    ------------------------------------------
    question - текст вопроса
    answer - текст ответа (WYSIWYG editor)
    image - путь до файла в файловой системе
    filename - название файла с расширением
    size - разрешение миниатюры изображения
    align_left - слева или справа находится картинка
    enabled - показывать эту запись или нет
    created - дата создания этй записи
    changed - дата последнего изменения этой записи
    position - положение этой записи
    ------------------------------------------
    Таблица в БД: faq_records """
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=1000)
    image = models.FileField(upload_to=get_faqpic_path, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    size = models.CharField(max_length=10, default=u'170x120')
    align_left = models.BooleanField(default=True)
    enabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']
        db_table = u'faq_records'
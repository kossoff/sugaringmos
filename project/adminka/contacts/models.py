# -*- coding: utf8 -*-
from django.db import models


# --- CONTACTS ------------------------------------------------------


class Contact(models.Model):
    """ Модель данных Contact предназначена
    для хранения контактных данных
    ------------------------------------------
    code - назначение поля
    name - название поля
    body - содержимое поля
    ------------------------------------------
    Таблица в БД: faq_records """
    code = models.CharField(max_length=10, default=u'code')
    name = models.CharField(max_length=20, default=u'name')
    body = models.CharField(max_length=1000, default=u'body')

    class Meta:
        db_table = u'contacts'
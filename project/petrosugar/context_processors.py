# -*- coding: utf8 -*-
from adminka.contacts.models import Contact
from adminka.services.models import Service


# --- CONTACTS CONTEXT PROCESSOR ------------------------------------


def contacts_context_processor(request):
    query = Contact.objects.all()
    values = query.values_list('code', 'body')
    con = {x: y for x, y in values}
    servmenu = Service.objects.all()
    return {'contacts': con, 'servmenu': servmenu}
from django.views.generic import ListView
from catalog.models import Contacts


class ContactsListView(ListView):
    model = Contacts
    extra_context = {
        'title': 'Контакты'
    }


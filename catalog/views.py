from django.shortcuts import render

from catalog.models import Product, Contacts


def home_page(request):
    queryset_length = Product.objects.count()
    if queryset_length >= 5:
        products = Product.objects.all()[queryset_length - 5:]
        for product in products:
            print(f'{product}\n')
    return render(request, 'catalog/home.html')


def contacts_page(request):
    return render(request, 'catalog/contacts.html', {'contacts':Contacts.objects.all()})

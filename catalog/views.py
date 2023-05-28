from django.shortcuts import render

from catalog.models import Product, Contacts


def home_page(request):
    queryset_length = Product.objects.count()
    if queryset_length >= 5:
        products = Product.objects.all()[queryset_length - 5:]
        for product in products:
            print(f'{product}\n')

    context = {
        'object_list': Product.objects.all(),
        'title': 'Домашняя страница'
    }
    return render(request, 'catalog/index.html', context)


def contacts_page(request):
    context = {
        'object_list': Contacts.objects.all(),
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)

def products_page(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Продукты'
    }
    return render(request, 'catalog/products.html', context)

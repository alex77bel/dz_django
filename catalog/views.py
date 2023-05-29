from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from catalog.models import Product, Contacts
from catalog.forms import UploadFileForm

PRODUCTS_PER_PAGE = 9


def home_page(request):
    object_list = Product.objects.all()
    paginator = Paginator(object_list, PRODUCTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': 'Домашняя страница'
    }
    return render(request, 'catalog/index.html', context)


def contacts_page(request):
    context = {
        'object_list': Contacts.objects.all(),
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product_page(request, product_id):
    context = {
        'object': Product.objects.get(pk=product_id),
        'title': 'Товар'
    }
    return render(request, 'catalog/product.html', context)


def add_product(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UploadFileForm
    context = {
        'form': form,
        'title': 'Новый продукт'
    }
    return render(request, 'catalog/add_product.html', context)

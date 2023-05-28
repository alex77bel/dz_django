from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home_page, contacts_page, products_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home'),
    path('contacts/', contacts_page, name='contacts'),
    path('products/', products_page, name='products'),

]
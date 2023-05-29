from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home_page, contacts_page, product_page, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home'),
    path('contacts/', contacts_page, name='contacts'),
    path('product/<int:product_id>/', product_page, name='product'),
    path('add_product/', add_product, name='add_product')

]

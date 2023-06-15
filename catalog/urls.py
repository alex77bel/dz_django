from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views.product_views import ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from catalog.views.blog_views import BlogView, BlogPostCreateView, BlogPostDetailView, BlogPostUpdateView, \
    BlogPostDeleteView
from catalog.views.contact_views import ContactsListView

app_name = CatalogConfig.name

urlpatterns = [

    path('contacts/', ContactsListView.as_view(), name='contacts'),

    path('', ProductsListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),

    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/create_post/', BlogPostCreateView.as_view(), name='create_post'),
    path('blog/post/<int:year>/<int:month>/<int:day>/<slug:slug>/', BlogPostDetailView.as_view(), name='post'),
    path('blog/update_post/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         BlogPostUpdateView.as_view(), name='update_post', ),
    path('blog/delete_post/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         BlogPostDeleteView.as_view(), name='delete_post'),

]

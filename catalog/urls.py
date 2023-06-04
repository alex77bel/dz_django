from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomePageListView, ContactsListView, ProductDetailView, ProductCreateView, \
    BlogView, BlogPostCreateView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home_page, name='home'),
    path('', HomePageListView.as_view(), name='home'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/create_post/', BlogPostCreateView.as_view(), name='create_post'),
    path('blog/post/<slug:slug>/', BlogPostDetailView.as_view(), name='post'),
    path('blog/update_post/<slug:slug>/', BlogPostUpdateView.as_view(), name='update_post',),
    path('blog/delete_post/<slug:slug>/', BlogPostDeleteView.as_view(), name='delete_post'),

]

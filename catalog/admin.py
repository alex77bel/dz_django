from django.contrib import admin
from .models import Category, Product

# Register your models here.

# admin.site.register(Category)
# admin.site.register(Product)


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
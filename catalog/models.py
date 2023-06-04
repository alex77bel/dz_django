from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', blank=False, null=False, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', blank=False, null=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', null=True, blank=True)
    price = models.FloatField(verbose_name='Цена', blank=False, null=False)
    date_create = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    date_modify = models.DateField(verbose_name='Дата изменения', auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', null=True)

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')

    def __str__(self):
        return f'Имя: {self.name}\nТелефон: {self.phone}\nE-mail: {self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ('name',)


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, verbose_name='Слаг', unique_for_date='created')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(verbose_name='Признак публикации', default=False)
    views = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def add_view(self):
        self.views += 1
        return self.views

    def delete(self, *args, **kwargs):
        self.published = False
        self.save()

    def __str__(self):
        return f'Название статьи: {self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-created',)

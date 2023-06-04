from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Contacts, Post
from catalog.services import sendmail

PRODUCTS_PER_PAGE = 9


class HomePageListView(ListView):
    model = Product
    paginate_by = PRODUCTS_PER_PAGE
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Домашняя страница'
    }


class ContactsListView(ListView):
    model = Contacts
    extra_context = {
        'title': 'Контакты'
    }


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Просмотр продукта'
        return context_data


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'price', 'category']
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        'title': 'Создание продукта'
    }


class BlogPostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'preview', 'published')
    success_url = reverse_lazy('catalog:blog')
    extra_context = {
        'title': 'Создание статьи'
    }

    def form_valid(self, form):
        if form.is_valid:
            fields = form.save(commit=False)
            string = fields.title.translate(
                str.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                              "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"))
            fields.slug = slugify(string)
            fields.save()
        return super().form_valid(form)


class BlogView(ListView):
    model = Post
    template_name = 'catalog/blog.html'
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):  # добавление одного просмотра
        post = super().get_object()
        post.add_view()
        if post.views == 100:
            sendmail(f'Поздравляю, статья "{post.title}" набрала {post.views} просмотров')
        post.save()

        return post

    def get_context_data(self, **kwargs):  # получение 'title'
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Просмотр статьи'
        return context_data


class BlogPostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'preview', 'published')
    extra_context = {
        'title': 'Изменить статью'
    }

    def get_success_url(self):
        return reverse('catalog:post', args=[self.kwargs.get('slug')])


class BlogPostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('catalog:blog')

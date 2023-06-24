from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views import generic
from catalog.models import Product, Version

from catalog.forms import ProductForm, VersionForm

PRODUCTS_PER_PAGE = 6


class ProductsListView(generic.ListView):
    model = Product
    paginate_by = PRODUCTS_PER_PAGE
    extra_context = {
        'title': 'Продукты'
    }


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Просмотр продукта'
        return context_data


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        'title': 'Создание продукта'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        context_data['formset'] = version_formset()

        if self.request.method == 'POST':
            context_data['formset'] = version_formset(self.request.POST)
        else:
            context_data['formset'] = version_formset()
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        if form.is_valid():
            fields = form.save(commit=False)
            fields.user = self.request.user
            fields.save()
        return super().form_valid(form)


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'title': 'Изменение продукта'
    }

    def get_success_url(self):
        return reverse('catalog:update_product', args=[*self.kwargs.values()])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        context_data['formset'] = version_formset()

        if self.request.method == 'POST':
            context_data['formset'] = version_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = version_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'catalog/confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        'title': 'Удаление'
    }

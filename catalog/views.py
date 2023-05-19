from django.shortcuts import render


# Create your views here.


def home_page(request):
    return render(request, 'catalog/home.html')


def contacts_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        print(f'Имя: {name}\nТелефон: {phone}\nE-mail: {email}')

    return render(request, 'catalog/contacts.html')

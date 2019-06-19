from django.shortcuts import render
from .models import Phone, Samsung, Apple, Xiaomi


def show_catalog(request):
    phones = list()
    optionals = list()
    samsung = Samsung.objects.all()
    apple = Apple.objects.all()
    xiaomi = Xiaomi.objects.all()
    for phone in samsung:
        phones.append(phone.phone)
        optionals.append(phone.other)

    for phone in apple:
        phones.append(phone.phone)
        optionals.append(phone.other)

    for phone in xiaomi:
        phones.append(phone.phone)
        optionals.append(phone.other)

    template = 'catalog.html'
    context = {'phones': phones,
               'optionals': optionals}
    return render(
        request,
        template,
        context
    )

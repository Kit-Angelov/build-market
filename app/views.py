from django.shortcuts import render


def products(request):
    context = {'active': 'products'}
    return render(request, 'app/products.html', context=context)


def stores(request):
    context = {'active': 'stores'}
    return render(request, 'app/stores.html', context=context)


def services(request):
    context = {'active': 'services'}
    return render(request, 'app/services.html', context=context)


def contractors(request):
    context = {'active': 'contractors'}
    return render(request, 'app/contractors.html', context=context)
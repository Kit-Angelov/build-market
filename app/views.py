from django.shortcuts import render, Http404
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def products(request):
    if request.method == 'GET':
        product_list = models.Product.objects.all()
        paginator = Paginator(product_list, 12)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'products': products,
                   'active': 'products'}
        return render(request, 'app/products.html', context=context)


def product(request, pk):
    if request.method == 'GET':
        try:
            product = models.Product.objects.get(id=pk)
        except:
            raise Http404("Product does not exist")
        context = {'product': product}
        return render(request, 'app/product.html', context=context)


def stores(request):
    if request.method == 'GET':
        store_list = models.Store.objects.all()
        paginator = Paginator(store_list, 12)
        page = request.GET.get('page')
        try:
            stores = paginator.page(page)
        except PageNotAnInteger:
            stores = paginator.page(1)
        except EmptyPage:
            stores = paginator.page(paginator.num_pages)
        context = {'stores': stores,
                   'active': 'stores'}
        return render(request, 'app/stores.html', context=context)


def store(request, pk):
    if request.method == 'GET':
        try:
            store = models.Store.objects.get(id=pk)
        except:
            raise Http404("Store does not exist")
        context = {'store': store}
        return render(request, 'app/store.html', context=context)


def services(request):
    context = {'active': 'services'}
    return render(request, 'app/services.html', context=context)


def contractors(request):
    if request.method == 'GET':
        contractor_list = models.Contractor.objects.all()
        paginator = Paginator(contractor_list, 12)
        page = request.GET.get('page')
        try:
            contractors = paginator.page(page)
        except PageNotAnInteger:
            contractors = paginator.page(1)
        except EmptyPage:
            contractors = paginator.page(paginator.num_pages)
        context = {'contractors': contractors,
                   'active': 'contractors'}
        return render(request, 'app/contractors.html', context=context)
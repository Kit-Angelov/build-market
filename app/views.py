from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json


def products(request):
    if request.method == 'GET':
        product_list = models.Product.objects.all().order_by('id')
        paginator = Paginator(product_list, 2)
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


def services(request):
    if request.method == 'GET':
        service_list = models.Service.objects.all().order_by('id')
        paginator = Paginator(service_list, 2)
        page = request.GET.get('page')
        try:
            services = paginator.page(page)
        except PageNotAnInteger:
            services = paginator.page(1)
        except EmptyPage:
            services = paginator.page(paginator.num_pages)
        context = {'services': services,
                   'active': 'services'}
        return render(request, 'app/services.html', context=context)


def about(request):
    if request.method == 'GET':
        return render(request, 'app/about.html')


def get_tags_services(request):
    if request.method == "GET":
        query = request.GET.get("query")
        if query is None:
            return JsonResponse({"resutl": None})
        tags = models.TagService.objects.filter(text__icontains=str(query).lower())[:5]
        response_dict = {"result": [x for x in tags.values()]}
        return JsonResponse(response_dict)


def get_tags_products(request):
    if request.method == "GET":
        query = request.GET.get("query")
        if query is None:
            return JsonResponse({"resutl": None})
        tags = models.TagProduct.objects.filter(text__icontains=str(query).lower())[:5]
        response_dict = {"result": [x for x in tags.values()]}
        return JsonResponse(response_dict)

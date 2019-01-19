from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.response import Response
from .serializers import ProductsListSerializer


# def products(request):
#     if request.method == 'GET':
#         product_list = models.Product.objects.all().order_by('id')
#         paginator = Paginator(product_list, 2)
#         page = request.GET.get('page')
#         try:
#             products = paginator.page(page)
#         except PageNotAnInteger:
#             products = paginator.page(1)
#         except EmptyPage:
#             products = paginator.page(paginator.num_pages)
#         context = {'products': products,
#                    'active': 'products'}
#         return render(request, 'app/products.html', context=context)
#     if request.method == 'POST':
#         search_text = request.POST.get('search_text')
#         tags = models.TagProduct.objects.filter(text__icontains=str(search_text).lower())
#         product_list = models.Product.objects.filter(tagproduct__in=tags)
#         product_set = list(set(product_list))
#         paginator = Paginator(product_set, 2)
#         page = request.GET.get('page')
#         try:
#             products = paginator.page(page)
#         except PageNotAnInteger:
#             products = paginator.page(1)
#         except EmptyPage:
#             products = paginator.page(paginator.num_pages)
#         context = {'products': products,
#                    'active': 'products'}
#         return render(request, 'app/products.html', context=context)
#
#
# def services(request):
#     if request.method == 'GET':
#         service_list = models.Service.objects.all().order_by('id')
#         paginator = Paginator(service_list, 2)
#         page = request.GET.get('page')
#         try:
#             services = paginator.page(page)
#         except PageNotAnInteger:
#             services = paginator.page(1)
#         except EmptyPage:
#             services = paginator.page(paginator.num_pages)
#         context = {'services': services,
#                    'active': 'services'}
#         return render(request, 'app/services.html', context=context)
#
#
# def about(request):
#     if request.method == 'GET':
#         return render(request, 'app/about.html')
#
#
# def get_tags_services(request):
#     if request.method == "GET":
#         query = request.GET.get("query")
#         if query is None:
#             return JsonResponse({"resutl": None})
#         tags = models.TagService.objects.filter(text__icontains=str(query).lower())[:5]
#         response_dict = {"result": [x for x in tags.values()]}
#         return JsonResponse(response_dict)
#
#
# def get_tags_products(request):
#     if request.method == "GET":
#         query = request.GET.get("query")
#         if query is None:
#             return JsonResponse({"resutl": None})
#         tags = models.TagProduct.objects.filter(text__icontains=str(query).lower())[:5]
#         response_dict = {"result": [x for x in tags.values()]}
#         return JsonResponse(response_dict)
#
#
# class Products(APIView):
#     serializer_class = ProductsListSerializer
#     pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
#
#     def get(self, request):
#         product_list = models.Product.objects.all().order_by('id')
#         page = self.paginate_queryset(product_list)
#         if page is not None:
#             serializer = self.serializer_class(page, many=True, context={'request': request})
#             print(serializer.data)
#             return self.get_paginated_response(serializer.data)
#
#     @property
#     def paginator(self):
#         if not hasattr(self, '_paginator'):
#             if self.pagination_class is None:
#                 self._paginator = None
#             else:
#                 self._paginator = self.pagination_class()
#         return self._paginator
#
#     def paginate_queryset(self, queryset):
#         if self.paginator is None:
#             return None
#         return self.paginator.paginate_queryset(queryset, self.request, view=self)
#
#     def get_paginated_response(self, data):
#         assert self.paginator is not None
#         return self.paginator.get_paginated_response(data)
#
#
# class Product(APIView):
#
#     def get(self, request, pk):
#         Response('pk')


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductsListSerializer
    queryset = models.Product.objects.all()

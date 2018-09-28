from django.urls import path
from . import views
from django.conf import settings

app_name = 'app'
urlpatterns = [
    path('', views.products),
    path('products/<pk>', views.product),
    path('stores', views.stores),
    path('stores/<pk>', views.store),
    path('services', views.services),
    path('contractors', views.contractors),
]
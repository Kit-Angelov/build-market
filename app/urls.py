from django.urls import path
from . import views
from django.conf import settings

app_name = 'app'
urlpatterns = [
    path('', views.products),
    path('services', views.services),
    path('about', views.about),
    path('get_tags_services', views.get_tags_services),
    path('get_tags_products', views.get_tags_products),
]
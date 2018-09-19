from django.urls import path
from . import views
from django.conf import settings

app_name = 'app'
urlpatterns = [
    path('', views.products),
    path('stores', views.stores),
    path('services', views.services),
    path('contractors', views.contractors),
]
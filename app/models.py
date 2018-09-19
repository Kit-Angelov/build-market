from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class ProductFeature(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    text = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)


class ProductUse(models.Model):
    text = models.CharField(max_length=255, primary_key=True)
    products = models.ManyToManyField(Product)


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to='product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
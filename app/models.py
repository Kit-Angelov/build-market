from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    choord = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    work_time_start = models.TimeField(blank=True, null=True)
    work_time_end = models.TimeField(blank=True, null=True)
    work_days = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class StorePhoto(models.Model):
    photo = models.ImageField(upload_to='store')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo.name


class ProductFeature(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {}'.format(self.title, self.text)


class ProductUse(models.Model):
    text = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.text


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    views = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    site_link = models.TextField(blank=True, null=True)
    store = models.ForeignKey(Store, blank=True, null=True, on_delete=models.CASCADE)
    features = models.ManyToManyField(ProductFeature, blank=True, null=True)
    uses = models.ManyToManyField(ProductUse, blank=True, null=True)
    actual = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to='product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo.name

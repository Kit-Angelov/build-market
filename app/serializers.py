from rest_framework import serializers
from .models import Product


class ProductsListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

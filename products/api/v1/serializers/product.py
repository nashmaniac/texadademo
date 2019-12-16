from rest_framework import serializers
from products.models import Product


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

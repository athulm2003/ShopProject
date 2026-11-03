from rest_framework import serializers
from .models import Category, ProductDb


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDb
        fields = "__all__"
from rest_framework import serializers
from .models import Category, Images, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category_name']


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['image']


class ProductListSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=False, read_only=True)
    product_image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'product_name', 'category', 'price', 'is_new',
            'product_image'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=False, read_only=True)
    product_image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'product_name', 'category', 'price', 'is_new',
            'product_image', 'composition', 'product_description',
            'mass'
        ]

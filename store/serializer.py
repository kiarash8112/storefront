from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    def create(self, validated_data):
        product = Product(**validated_data)
        product.other = 1
        product.save()
        return product

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ReviewSerializer(serializers.Serializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description', 'product']

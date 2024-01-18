from rest_framework import serializers
from .models import Order
from products.models import Product
from products.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'total', 'created_at']

    def validate_products(self, products):
        if not products:
            raise serializers.ValidationError("Pelo menos um produto é necessário.")
        return products
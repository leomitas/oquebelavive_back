from rest_framework import serializers
from .models import Order
from products.models import Product
from products.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'products', 'created_at']
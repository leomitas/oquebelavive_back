from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Order
from .serializers import OrderSerializer
from products.models import Product
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # lookup_field = "id"

    def create(self, request, *args, **kwargs):
        products_ids = request.data.get("products", [])

        for product_id in products_ids:
            product = Product.objects.filter(id=product_id).first()
            if product:
                product.sold += 1
                product.save()
            else:
                return Response({"message": f"Produto com ID {product_id} não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        new_order = Order.objects.create()

        new_order.products.add(*products_ids)

        serializer = self.get_serializer(new_order)
        return Response(serializer.data, status=201)
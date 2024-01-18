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

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        products_ids = request.data.get("products", [])
        total = 0
        for product_id in products_ids:
            product = Product.objects.filter(id=product_id).first()
            product.sold += 1
            product.save()
            total += product.price

        new_order = Order.objects.create(total=total)
        new_order.products.add(*products_ids)

        serializer = self.get_serializer(new_order)
        return Response(serializer.data, status=201)
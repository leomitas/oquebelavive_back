from django.db import models
from products.models import Product
from users.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product)
    total = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
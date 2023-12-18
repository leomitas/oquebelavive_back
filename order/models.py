from django.db import models
from products.models import Product
from rest_framework import serializers

# Create your models here.
class Order(models.Model):
    products = models.ManyToManyField(Product)

    created_at = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     super(Order, self).save(*args, **kwargs)

    #     for product in self.products.all():
    #         product.sold += 1
    #         product.save()
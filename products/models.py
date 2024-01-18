from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    sold = models.IntegerField(null=False, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Generated by Django 5.0 on 2023-12-18 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_product_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
    ]
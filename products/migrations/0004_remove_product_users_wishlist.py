# Generated by Django 4.1.2 on 2022-11-21 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_users_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users_wishlist',
        ),
    ]
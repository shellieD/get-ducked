# Generated by Django 4.1.2 on 2022-11-16 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_rename_reviews_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='products',
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_rename_status_review_approved_remove_review_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='approved',
        ),
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Added')], default=0),
        ),
    ]

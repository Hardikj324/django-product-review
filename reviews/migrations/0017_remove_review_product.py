# Generated by Django 5.1.1 on 2025-02-19 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0016_product_review_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
    ]

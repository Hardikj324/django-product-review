# Generated by Django 5.1.1 on 2025-02-10 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_userregister_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review', to='reviews.userregister'),
        ),
    ]

# Generated by Django 5.1.1 on 2024-12-25 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_userregister_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregister',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='userregister',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='userregister',
            name='Username',
        ),
    ]

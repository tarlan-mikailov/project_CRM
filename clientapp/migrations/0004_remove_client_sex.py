# Generated by Django 4.2.6 on 2023-11-01 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0003_client_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='sex',
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0013_alter_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=16),
        ),
    ]

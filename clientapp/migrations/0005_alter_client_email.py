# Generated by Django 4.2.6 on 2023-11-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0004_remove_client_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]

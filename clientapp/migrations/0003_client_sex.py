# Generated by Django 4.2.6 on 2023-11-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0002_alter_client_birthday_alter_client_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='sex',
            field=models.CharField(default=None, max_length=15),
        ),
    ]

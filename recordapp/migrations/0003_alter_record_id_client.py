# Generated by Django 4.2.6 on 2023-11-06 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0010_alter_client_email'),
        ('recordapp', '0002_alter_record_id_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientapp.client'),
        ),
    ]

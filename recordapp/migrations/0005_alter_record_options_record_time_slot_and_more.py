# Generated by Django 4.2.6 on 2023-11-30 17:10

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientapp', '0018_alter_clientphoto_image'),
        ('recordapp', '0004_alter_record_id_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['-date', 'time_slot']},
        ),
        migrations.AddField(
            model_name='record',
            name='time_slot',
            field=models.SmallIntegerField(default=9),
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together={('date', 'id_staff', 'id_client')},
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.CheckConstraint(check=models.Q(('date__gte', datetime.date(2023, 11, 30))), name='date__gte_today'),
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.CheckConstraint(check=models.Q(('price__gt', 0)), name='price__gte_0'),
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.CheckConstraint(check=models.Q(('time_slot__gte', 5)), name='time_slot__gte_5'),
        ),
        migrations.AlterModelTable(
            name='record',
            table='Record',
        ),
        migrations.RemoveField(
            model_name='record',
            name='duration',
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-12 22:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_refueling_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refueling',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='refueling',
            name='date_field',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
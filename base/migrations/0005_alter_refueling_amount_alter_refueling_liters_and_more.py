# Generated by Django 4.0.6 on 2022-07-12 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_refueling_created_alter_refueling_date_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refueling',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='refueling',
            name='liters',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='refueling',
            name='price_per_liter',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
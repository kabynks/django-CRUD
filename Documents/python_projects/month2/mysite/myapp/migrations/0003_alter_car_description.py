# Generated by Django 4.2 on 2024-01-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_car_capacity_alter_car_horse_power_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

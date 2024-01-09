# Generated by Django 4.2 on 2024-01-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('date_of_manufacture', models.DateField(auto_now_add=True)),
                ('horse_power', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
    ]

# Generated by Django 4.2 on 2024-01-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_car_horse_power'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(default=1, upload_to='myapp/media'),
            preserve_default=False,
        ),
    ]

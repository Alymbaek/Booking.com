# Generated by Django 5.1.2 on 2024-10-29 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_hotel_hotel_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='city_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='country_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='country_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='hotelimage',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_images', to='booking.hotel'),
        ),
    ]

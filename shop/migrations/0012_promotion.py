# Generated by Django 4.0.5 on 2022-06-19 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_brand_rating_equipment_in_stock_equipment_is_promo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название преимущества')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-16 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_equipmentcategory_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='shop.equipmentcategory', verbose_name='Тип'),
        ),
    ]
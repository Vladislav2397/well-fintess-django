# Generated by Django 4.0.3 on 2022-04-16 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rename_equipmenttype_equipmentcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentcategory',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shop.equipmentfamily'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-19 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='promotion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.promotion', verbose_name='Название акции'),
        ),
    ]
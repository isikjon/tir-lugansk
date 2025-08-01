# Generated by Django 5.2.4 on 2025-07-29 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAnalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('analog_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analog_for', to='shop.product', verbose_name='Аналог')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analogs', to='shop.product', verbose_name='Основной товар')),
            ],
            options={
                'verbose_name': 'Аналог товара',
                'verbose_name_plural': 'Аналоги товаров',
                'unique_together': {('product', 'analog_product')},
            },
        ),
    ]

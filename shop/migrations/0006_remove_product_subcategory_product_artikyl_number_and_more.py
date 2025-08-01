# Generated by Django 5.2.4 on 2025-07-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='artikyl_number',
            field=models.CharField(blank=True, max_length=100, verbose_name='Дополнительный номер товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='cross_number',
            field=models.CharField(blank=True, max_length=100, verbose_name='Кросс-код товара'),
        ),
    ]

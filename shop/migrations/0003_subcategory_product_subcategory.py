# Generated by Django 5.2.4 on 2025-07-29 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productanalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='subcategories/', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='shop.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'ordering': ['parent', 'order', 'name'],
                'unique_together': {('parent', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.subcategory', verbose_name='Подкатегория'),
        ),
    ]

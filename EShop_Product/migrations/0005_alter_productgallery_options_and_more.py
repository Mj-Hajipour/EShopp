# Generated by Django 5.1.2 on 2024-12-21 17:44

import EShop_Product.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop_Product', '0004_productgallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productgallery',
            options={'verbose_name': 'تصویر', 'verbose_name_plural': 'تصاویر'},
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(blank=True, upload_to=EShop_Product.models.upload_gallery_image_path, verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EShop_Product.product', verbose_name='برای محصول'),
        ),
    ]

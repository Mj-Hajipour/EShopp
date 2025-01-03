# Generated by Django 5.1.2 on 2024-11-11 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop_Product', '0002_alter_product_options_alter_product_active_and_more'),
        ('EShop_tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'تگ/برچسب', 'verbose_name_plural': 'تگ ها/بر چسب ها'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='active',
            field=models.BooleanField(default=True, verbose_name='غیر فعال'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='EShop_Product.product', verbose_name='محصولات'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(verbose_name='عنوان جستجو'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت'),
        ),
    ]

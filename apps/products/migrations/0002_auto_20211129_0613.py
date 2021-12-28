# Generated by Django 3.2.9 on 2021-11-29 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Артикул', 'verbose_name_plural': 'Артикулы'},
        ),
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='bouquet_care',
            field=models.TextField(blank=True, null=True, verbose_name='Уход за букетом'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='categories.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='discount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='equipment',
            field=models.TextField(blank=True, null=True, verbose_name='Комплектация'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='is_new',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Новый ли продукт?'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_items', to='products.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='specifications',
            field=models.TextField(blank=True, null=True, verbose_name='Спецификация'),
        ),
    ]

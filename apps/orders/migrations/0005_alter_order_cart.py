# Generated by Django 3.2.9 on 2021-12-27 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_alter_cartitem_cart'),
        ('orders', '0004_auto_20211129_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='carts.cart', verbose_name='Корзина'),
        ),
    ]

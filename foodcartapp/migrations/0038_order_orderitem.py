# Generated by Django 4.1.3 on 2022-11-28 17:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0037_auto_20210125_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(db_index=True, max_length=50, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, db_index=True, default='', max_length=50, verbose_name='Фамилия')),
                ('address', models.TextField(verbose_name='адрес')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region='RU', verbose_name='номер телефона')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='foodcartapp.order', verbose_name='заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='foodcartapp.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'продукт в заказе',
                'verbose_name_plural': 'продукты в заказе',
                'db_table': 'order_items',
            },
        ),
    ]

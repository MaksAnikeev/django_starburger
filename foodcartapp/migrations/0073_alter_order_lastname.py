# Generated by Django 4.1.3 on 2023-01-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0072_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='lastname',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Фамилия'),
        ),
    ]

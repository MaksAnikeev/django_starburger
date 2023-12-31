# Generated by Django 3.2.15 on 2023-06-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCoordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, unique=True, verbose_name='адрес места')),
                ('lng', models.FloatField(blank=True, verbose_name='Долгота/Longitude')),
                ('lat', models.FloatField(blank=True, verbose_name='Широта/Latitude')),
            ],
            options={
                'verbose_name': 'координаты',
                'verbose_name_plural': 'координаты',
                'db_table': 'coordinate',
            },
        ),
    ]

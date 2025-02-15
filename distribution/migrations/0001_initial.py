# Generated by Django 5.1.6 on 2025-02-12 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('model', models.CharField(max_length=100, verbose_name='модель')),
                ('release_date', models.DateField(verbose_name='дата выхода на рынок')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ['-release_date'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('country', models.CharField(max_length=35, verbose_name='cтрана')),
                ('city', models.CharField(max_length=35, verbose_name='город')),
                ('street', models.CharField(max_length=35, verbose_name='улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='номер дома')),
                ('level', models.IntegerField(default=0, verbose_name='уровень в иерархии')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='долг перед поставщиком')),
                ('products', models.ManyToManyField(to='distribution.product', verbose_name='продукты')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='поставщик', to='distribution.unit')),
            ],
            options={
                'verbose_name': 'филиал',
                'verbose_name_plural': 'филиалы',
                'ordering': ['level'],
            },
        ),
    ]

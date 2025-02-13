from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='название'
    )

    model = models.CharField(
        max_length=100,
        verbose_name='модель'
    )

    release_date = models.DateField(
        verbose_name='дата выхода на рынок'
    )

    def __str__(self):
        return f'{self.name} ({self.model})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['-release_date']


class Unit(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='наименование'
    )

    products = models.ManyToManyField(
        Product,
        blank=True,
        verbose_name='продукты'
    )

    email = models.EmailField(
        verbose_name='электронная почта'
    )

    country = models.CharField(
        max_length=35,
        verbose_name='cтрана'
    )

    city = models.CharField(
        max_length=35,
        verbose_name='город'
    )

    street = models.CharField(
        max_length=35,
        verbose_name='улица'
    )

    house_number = models.CharField(
        max_length=10,
        verbose_name='номер дома'
    )

    level = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='уровень в иерархии'
    )

    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='supplied_units',
        verbose_name='поставщик'
    )

    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='долг перед поставщиком'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время добавления')

    def __str__(self):
        return f'{self.name} {self.country} г.{self.city}({self.email})'

    class Meta:
        verbose_name = 'филиал'
        verbose_name_plural = 'филиалы'
        ordering = ['level']


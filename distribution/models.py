from django.db import models


class Product(models.Model):
    """
    Модель для товаров

    Поля:
    name - Наименование товара, производитель
    model - Модель товара
    release_date - дата выхода товара на рынок
    """
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
    """
    Модель для филиала

    Поля:
    name - Наименование филиала
    products - Продукты, которые продаются в филиале
    email - Электронная почта для связи
    -АДРЕС-
    country - Страна, в которой находится филиала
    city - Город
    street - Улица
    house_number - Номер дома
    -----------------------------------------------
    level - Уровень филиала (от 0 до 3)
    0 - завод
    1 - реализация напрямую с завода
    2 - реализация через закупку у другого филиала
    -----------------------------------------------
    supplier - Поставщик товаров для реализации
    debt - Долг перед поставщиком в рублях с точностью до копеек
    created_at - Дата внесения в систему

    """
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


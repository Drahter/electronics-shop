from django.contrib import admin
from django.db import transaction
from django.urls import reverse
from django.utils.html import format_html

from distribution.models import Product, Unit


@admin.register(Product)
class AdminRegisterProduct(admin.ModelAdmin):
    """Отображение продуктов в админ-панели"""
    filter = 'name'


@admin.register(Unit)
class AdminRegisterProduct(admin.ModelAdmin):
    """
    Отображение филиалов в админ-панели

    Настроена фильтрация по городу расположения и уровню филиала.
    Реальзовано admin action для очистки долга перед поставщиком.

    В поле 'поставщик' выводится ссылка ка страницу соответствующего филиала,
    переход позможен из списка филиалов или со страницы с информацией.
    """

    list_display = ('name', 'level', 'city', 'email', 'supplier_link', 'debt')
    ordering = ('city', 'level')
    list_filter = ('city', 'level')
    search_fields = ('name', 'city', 'email')
    actions = ['reset_debt']

    def supplier_link(self, obj):
        """Ссылка на страницу поставщика"""
        if obj.supplier:
            return format_html('<a href="{}">{}</a>',
                               reverse('admin:distribution_unit_change', args=[obj.supplier.pk]),
                               obj.supplier.name)
        return '-'

    supplier_link.short_description = 'Поставщик'

    @admin.action(description='Обнулить долг')
    @transaction.atomic
    def reset_debt(self, request, queryset):
        """Действие, очищающее задолженность перед поставщиком"""
        for unit in queryset:
            unit.debt = 0.00
            unit.save()
        self.message_user(request, "Долг успешно обнулен для выбранных филиалов.")

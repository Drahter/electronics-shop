from django.contrib import admin

from django.contrib import admin

from distribution.models import Product, Unit


@admin.register(Product)
class AdminRegisterProduct(admin.ModelAdmin):
    filter = 'name'


@admin.register(Unit)
class AdminRegisterProduct(admin.ModelAdmin):
    filter = 'city'

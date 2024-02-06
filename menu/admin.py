from django.contrib import admin
from .models import MenuPoint, Menu, UnderPoint


@admin.register(MenuPoint)
class MenuPointAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['underpoint']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(UnderPoint)
class UnderPointAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['points']
    prepopulated_fields = {"slug": ("name",)}

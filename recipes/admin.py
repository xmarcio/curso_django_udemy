from django.contrib import admin

from . import models


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    model = models.Category


@admin.register(models.Recipe)
class Recipe(admin.ModelAdmin):
    model = models.Recipe

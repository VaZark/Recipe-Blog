from django.contrib import admin
from .models import *

class DirectionInlineAdmin(admin.TabularInline):
    model = Direction
    extra = 1


class IngredientDetailAdmin(admin.TabularInline):
    model = IngredientDetail
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [IngredientDetailAdmin, DirectionInlineAdmin]


# admin.site.register(Ingredient)
# admin.site.register(Cuisine)
# admin.site.register(CookingType)
# admin.site.register(Direction)
# admin.site.register(Measure)
admin.site.register(Author)
admin.site.register(Recipe, RecipeAdmin)
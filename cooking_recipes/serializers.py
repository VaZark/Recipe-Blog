from rest_framework import serializers
from . import models

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ['name']

class RecipeSerializer(serializers.ModelSerializer):
    # Maps to __str__ of the Ingredient that already exists in the Object
    # Meanwhile, SlugRelatedField can be used to target the field desired
    ingredients = serializers.StringRelatedField(many=True) 
    author = serializers.StringRelatedField()
    
    class Meta:
        model = models.Recipe
        fields = '__all__'

from rest_framework import serializers
from .models import *

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']

class RecipeSerializer(serializers.ModelSerializer):
    # Maps to __str__ of the Ingredient that already exists in the Object
    # Meanwhile, SlugRelatedField can be used to target the field desired
    ingredients = serializers.StringRelatedField(many=True) 
    author = serializers.StringRelatedField()
    cuisine = serializers.StringRelatedField()
    cook_type = serializers.StringRelatedField()

    class Meta:
        model = Recipe
        fields = '__all__'

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['id','type']

class CookingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingType
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
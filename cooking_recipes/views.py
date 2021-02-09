from django.shortcuts import render
from rest_framework import generics, filters

from .models import *
from .serializers import *

class RecipeListView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        cuisine_q = self.request.query_params.get('cuisine', None)
        if cuisine_q is not None:
            # For related keys, follow the relation and specify the field to be searched
            # Works with /recipes?cuisine=Value
            queryset = queryset.filter(cuisine__type=cuisine_q)
        return queryset


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CuisineListView(generics.ListCreateAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer

    # For create validate, check if it already exists (with ignorecase)

class CuisineRetrieveView(generics.RetrieveAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer

class CookingTypeListView(generics.ListCreateAPIView):
    queryset = CookingType.objects.all()
    serializer_class = CookingTypeSerializer

    # For create validate, check if it already exists (with ignorecase)

class CookingTypeRetrieveView(generics.RetrieveAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # For create validate, check if it already exists (with ignorecase)

class AuthorRetrieveView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

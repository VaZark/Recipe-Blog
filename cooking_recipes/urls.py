from django.urls import path

from . import views

urlpatterns = [
    path('recipes/', views.RecipeListView.as_view()),
    path('recipes/<int:pk>', views.RecipeDetailView.as_view()),
    path('cuisines/', views.CuisineListView.as_view()),
    path('cuisines/<int:pk>', views.CuisineRetrieveView.as_view()),
    path('authors/', views.AuthorListView.as_view()),
    path('authors/<int:pk>', views.AuthorRetrieveView.as_view()),
    path('cook_styles/', views.CookingTypeListView.as_view()),
    path('cook_styles/<int:pk>', views.CookingTypeRetrieveView.as_view()),
]
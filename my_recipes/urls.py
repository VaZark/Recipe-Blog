from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include('cooking_recipes.urls')),
    path('', index, name="index") # Serve React build
]

from django.urls import path
from .views import DisplayElementsView, RecipesView  # Импортируем функцию recipes_view


app_name = 'Game'
urlpatterns = [
    path('', DisplayElementsView.as_view(), name='display_elements'),
    path('recipes', RecipesView.as_view(), name='recipes_view'),  # Используем имя 'recipes_view'
]

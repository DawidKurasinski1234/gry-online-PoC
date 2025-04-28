"""
URL configuration for project_game project.
"""
from django.contrib import admin
from django.urls import path
from app_game import views
# Usunięto: from app_game.views import * - nie jest to najlepsza praktyka

urlpatterns = [
    path('', views.index, name='home_page'),  # Zmieniono nazwę na 'home' dla spójności
    path('details/<int:id>/', views.details, name='game_details'),  # Zakładam, że to jest widok szczegółów
    path('admin/', admin.site.urls),
    path('games/kk/', views.kolko_i_krzyzyk_view, name='kolko_i_krzyzyk'),
    path('games/snake/', views.snake_view, name='snake'),
    path('games/tetris/', views.tetris_view, name='tetris'),
    path('games/unity/', views.unity_view, name='unity_vr'),  # Poprawiono ścieżkę na małe litery
]
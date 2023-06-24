
from django.urls import path
from . import views

app_name = "mata_mosca"

urlpatterns = [
    path('app/', views.view_app, name="app"),
    path('game_over/', views.view_game_over, name="game_over"),
    path('', views.view_inicio, name="inicio"),
    path('victory/', views.view_victory, name="victory"),
]

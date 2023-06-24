
from django.urls import path
from . import views

app_name = "uber"

urlpatterns = [
    path('contato/', views.view_contato, name="contato"),
    path('', views.view_inicio, name="inicio"),
    path('login/', views.view_login, name="login"),
    path('mobile/', views.view_mobile, name='mobile'),
    path('register_motorista/', views.view_register_motorista, name="register_motorista"),
    path('register/', views.view_register, name="register"),
    path('servicos/', views.view_servicos, name='servicos'),
    path('sobre/', views.view_sobre, name="sobre"),
    path('uber_eats/', views.view_uber_eats, name="uber_eats"),
]


from django.urls import path
from . import views

app_name = "orcamento"

urlpatterns = [
    path('', views.view_inicio, name="inicio"),
    path('consulta/', views.view_consulta, name="consulta"),
]

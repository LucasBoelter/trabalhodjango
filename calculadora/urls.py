from django.contrib import admin
from django.urls import path
from . import views

app_name = "calculadora"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.view_inicio, name="inicio"),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('calculadora/', include("calculadora.urls")),
    path('mata_mosca/', include("mata_mosca.urls")),
    path('orcamento/', include("orcamento.urls")),
    path('uber/', include("uber.urls")),
]

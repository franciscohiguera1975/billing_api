from django.urls import path
from . import views

urlpatterns = [
    path('basics/area-triangulo', views.area_triangulo),
    path('basics/tabla-multiplicar', views.tabla_multiplicar),
    path('basics/contar-mayores', views.contar_mayores),
    path('basics/sumar-consecutivos', views.sumar_consecutivos),   
    path('basics/promedio', views.promedio),
]

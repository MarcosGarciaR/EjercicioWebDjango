from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('doctores/' , views.lista_doctores, name='mostrar_doctores'),
    path('pacientes/' , views.lista_pacientes, name='mostrar_pacientes'),
    path('habitaciones/' , views.lista_habitaciones, name='mostrar_habitaciones'),
]
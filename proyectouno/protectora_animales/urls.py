from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('animals/', views.animals_list, name='animals_list'),
    path('protectoras/', views.protectoras_list, name='protectoras_list'),
    path('colaboradores/', views.colaboradores_list, name='colaboradores_list'),
]
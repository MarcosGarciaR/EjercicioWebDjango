from django.shortcuts import render
from .models import Doctores, Pacientes, Habitaciones
# Create your views here.

def inicio(request):
    return render(request, 'hospital/pagina_inicio.html', {})

def lista_doctores(request):
    doctores = Doctores.objects.all()
    return render(request, 'hospital/vista_doctores.html', {'mostrar_doctores' : doctores})
    
def lista_pacientes(request):
    pacientes = Pacientes.objects.all()
    return render(request, 'hospital/vista_pacientes.html', {'mostrar_pacientes' : pacientes})
    
def lista_habitaciones(request):
    habitaciones = Habitaciones.objects.all()
    return render(request, 'hospital/vista_habitaciones.html', {'mostrar_habitaciones' : habitaciones})

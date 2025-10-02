from django.shortcuts import render
from .models import Animal, Colaborador, Protectora

# Create your views here.
def pagina_inicio(request):
    return render(request, 'protectora_animales/pagina_inicio.html', {})

def animals_list(request):
    animales = Animal.objects.all()
    return render(request, 'protectora_animales/animals_list.html', {'animales_mostrar' : animales})


def protectoras_list(request):
    protectoras = Protectora.objects.all()
    return render(request, 'protectora_animales/protectoras_list.html', {'protectoras_mostrar' : protectoras})


def colaboradores_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'protectora_animales/colaboradores_list.html', {'colaboradores_mostrar' : colaboradores})
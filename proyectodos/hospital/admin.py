from django.contrib import admin
from .models import Doctores, Habitaciones, Pacientes

# Register your models here.

admin.site.register(Doctores)
admin.site.register(Habitaciones)
admin.site.register(Pacientes)
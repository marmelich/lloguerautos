from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Automobil)
class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'model', 'matricula')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('automobil', 'user', 'data_inici', 'data_fi')
    list_filter = ('data_inici', 'data_fi', 'automobil')


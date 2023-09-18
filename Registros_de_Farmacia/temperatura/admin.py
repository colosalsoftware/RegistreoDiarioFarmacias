from django.contrib import admin
from .models import RegistroTemperatura

@admin.register(RegistroTemperatura)
class RegistroTemperaturaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'valor_temperatura')
    list_filter = ('fecha',)
    search_fields = ('fecha', 'valor_temperatura')

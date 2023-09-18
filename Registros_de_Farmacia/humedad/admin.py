from django.contrib import admin
from .models import RegistroHumedad

@admin.register(RegistroHumedad)
class RegistroHumedadAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'valor_humedad')
    list_filter = ('fecha',)
    search_fields = ('fecha', 'valor_humedad')

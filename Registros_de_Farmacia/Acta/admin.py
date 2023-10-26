from django.contrib import admin
from .models import Deposito, Medicamento, Laboratorio, Firma, RecepcionMedicamento, ActaRecepcion

class DepositoAdmin(admin.ModelAdmin):
    list_display = ['nombre_Deposito']

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre_Medicamento']

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ['nombre_Laboratorio']

class FirmaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'imagen']

class RecepcionMedicamentoAdmin(admin.ModelAdmin):
    list_display = ['medicamento', 'laboratorio', 'registro_invima', 'lote', 'cantidad', 'fecha_vencimiento', 'cumple_norma']
    list_filter = ['medicamento', 'laboratorio']

class ActaRecepcionAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'deposito', 'factura']
    list_filter = ['deposito']
    filter_horizontal = ['recepcion_medicamentos']

# Registra tus modelos personalizados de administración
admin.site.register(Deposito, DepositoAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Firma, FirmaAdmin)
admin.site.register(RecepcionMedicamento, RecepcionMedicamentoAdmin)
admin.site.register(ActaRecepcion, ActaRecepcionAdmin)

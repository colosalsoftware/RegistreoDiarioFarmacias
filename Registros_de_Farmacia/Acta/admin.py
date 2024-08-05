from django.contrib import admin
from dal import autocomplete
from django import forms
from .models import Deposito, Medicamento, Laboratorio, Firma, RecepcionMedicamento, ActaRecepcion

class DepositoAdmin(admin.ModelAdmin):
    list_display = ['nombre_Deposito']

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre_Medicamento']
    search_fields = ['nombre_Medicamento']
    ordering = ['nombre_Medicamento']

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ['nombre_Laboratorio']

class FirmaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'imagen']

class RecepcionMedicamentoForm(forms.ModelForm):
    medicamento = forms.ModelChoiceField(
        queryset=Medicamento.objects.all(),
        widget=autocomplete.ModelSelect2(url='medicamento-autocomplete')
    )
    laboratorio = forms.ModelChoiceField(
        queryset=Laboratorio.objects.all(),
        widget=autocomplete.ModelSelect2(url='laboratorio-autocomplete')
    )

    class Meta:
        model = RecepcionMedicamento
        fields = '__all__'

class RecepcionMedicamentoAdmin(admin.ModelAdmin):
    form = RecepcionMedicamentoForm
    list_display = ['medicamento', 'laboratorio', 'registro_invima', 'lote', 'cantidad', 'fecha_vencimiento', 'cumple_norma']
    list_filter = ['laboratorio']
    search_fields = ['medicamento__nombre_Medicamento', 'lote']
    ordering = ['medicamento__nombre_Medicamento']

class ActaRecepcionForm(forms.ModelForm):
    deposito = forms.ModelChoiceField(
        queryset=Deposito.objects.all(),
        widget=autocomplete.ModelSelect2(url='deposito-autocomplete')
    )

    class Meta:
        model = ActaRecepcion
        fields = '__all__'

class ActaRecepcionAdmin(admin.ModelAdmin):
    form = ActaRecepcionForm
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

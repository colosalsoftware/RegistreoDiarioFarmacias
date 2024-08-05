from django.shortcuts import render, get_object_or_404
from humedad.models import RegistroHumedad
from temperatura.models import RegistroTemperatura
from Acta.models import ActaRecepcion, RecepcionMedicamento, Medicamento,Laboratorio,Deposito
import plotly.express as px
from plotly.offline import plot
import pandas as pd
import datetime as dt
from dal import autocomplete

# Create your views here.
def home(request):
    return render(request,'home.html')

def registros_humedad_temperatura(request):
    # Obtener los valores del rango de fechas del formulario
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Convertir las fechas a objetos datetime, si se han proporcionado
    if fecha_inicio and fecha_fin:
        fecha_inicio = dt.datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin = dt.datetime.strptime(fecha_fin, '%Y-%m-%d')
        
        # Filtrar los registros por el rango de fechas
        registrosh = RegistroHumedad.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
        registrost = RegistroTemperatura.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
    else:
        # Si no se proporcionan fechas, se obtienen todos los registros
        registrosh = RegistroHumedad.objects.all()
        registrost = RegistroTemperatura.objects.all()

    # Crear DataFrames y gráficos para humedad
    data_frameh = pd.DataFrame(list(registrosh.values('fecha', 'valor_humedad')))
    figh = px.line(
        data_frameh,
        x='fecha',
        y='valor_humedad',
        title='Registros de Humedad',
        labels={'fecha': 'Fecha', 'valor_humedad': 'Valor de Humedad'},
    )
    figh.update_traces(line=dict(color='#99FFFF', width=2))
    figh.update_layout(
        plot_bgcolor='#666666',
        paper_bgcolor='#666666',
        font=dict(color='white'),
        title=dict(font=dict(size=26), x=0.5),
        xaxis_title='Fecha',
        yaxis_title='Valor de Humedad',
        xaxis=dict(gridcolor='gray'),
        yaxis=dict(gridcolor='gray'),
    )
    divh = figh.to_html()

    # Crear DataFrames y gráficos para temperatura
    data_framet = pd.DataFrame(list(registrost.values('fecha', 'valor_temperatura')))
    figt = px.line(
        data_framet,
        x='fecha',
        y='valor_temperatura',
        title='Registros de Temperatura',
        labels={'fecha': 'Fecha', 'valor_humedad': 'Valor de temperatura'},
    )
    figt.update_traces(line=dict(color='#61FF61', width=2))
    figt.update_layout(
        plot_bgcolor='#666666',
        paper_bgcolor='#666666',
        font=dict(color='white'),
        title=dict(font=dict(size=26), x=0.5),
        xaxis_title='Fecha',
        yaxis_title='Valor de Temperatura',
        xaxis=dict(gridcolor='gray'),
        yaxis=dict(gridcolor='gray'),
    )
    divt = figt.to_html()

    return render(request, 'registros_humedad_temperatura.html', {
        'graficohumedad': divh,
        'graficotemperatura': divt,
        'fecha_inicio': fecha_inicio.strftime('%Y-%m-%d') if fecha_inicio else '',
        'fecha_fin': fecha_fin.strftime('%Y-%m-%d') if fecha_fin else ''
    })

def lista_actas(request):
    actas = ActaRecepcion.objects.all().order_by('-fecha')
    return render(request, 'lista_actas.html', {'actas': actas})

def buscar_acta(request):
    actas = None
    medicamento_id = request.GET.get('medicamento_id')
    lote = request.GET.get('lote')
    
    if medicamento_id or lote:
        recepciones = RecepcionMedicamento.objects.all()
        if medicamento_id:
            recepciones = recepciones.filter(medicamento_id=medicamento_id)
        if lote:
            recepciones = recepciones.filter(lote__icontains=lote)
        
        actas = ActaRecepcion.objects.filter(recepcion_medicamentos__in=recepciones).distinct()

    medicamentos = Medicamento.objects.all().order_by('nombre_Medicamento')
    return render(request, 'buscar_acta.html', {'medicamentos': medicamentos, 'actas': actas})

def detalle_acta(request, acta_id):
    acta = get_object_or_404(ActaRecepcion, pk=acta_id)
    recepciones = acta.recepcion_medicamentos.all()
    return render(request, 'detalle_acta.html', {'acta': acta, 'recepciones': recepciones})

class MedicamentoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Medicamento.objects.none()

        qs = Medicamento.objects.all()

        if self.q:
            qs = qs.filter(nombre_Medicamento__icontains=self.q)

        return qs
    
class LaboratorioAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Laboratorio.objects.none()

        qs = Laboratorio.objects.all()

        if self.q:
            qs = qs.filter(nombre_Laboratorio__icontains=self.q)

        return qs

class DepositoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Deposito.objects.none()

        qs = Deposito.objects.all()

        if self.q:
            qs = qs.filter(nombre_Deposito__icontains=self.q)

        return qs
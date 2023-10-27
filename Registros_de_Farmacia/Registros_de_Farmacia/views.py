from django.shortcuts import render, get_object_or_404
from humedad.models import RegistroHumedad
from temperatura.models import RegistroTemperatura
from Acta.models import ActaRecepcion, RecepcionMedicamento
import plotly.express as px
from plotly.offline import plot
import pandas as pd

# Create your views here.
def home(request):
    return render(request,'home.html')

def registros_humedad_temperatura(request):
    # Obtener los registros de humedad
    registrosh = RegistroHumedad.objects.all()

    # Crear el DataFrame a partir de los registrosh
    data_frameh = pd.DataFrame(list(registrosh.values('fecha', 'valor_humedad')))

    
    # Crear el gráfico de línea con estilos personalizados
    figh = px.line(
        data_frameh,
        x='fecha',
        y='valor_humedad',
        title='Registros de Humedad Históricos',  # Cambia el título
        labels={'fecha': 'Fecha', 'valor_humedad': 'Valor de Humedad'},  # Etiquetas personalizadas
    )

    # Personalizar el estilo del gráfico
    figh.update_traces(line=dict(color='#99FFFF', width=2))  # Cambia el color de la línea y el grosor

    # Confighurar el diseño del gráfico
    figh.update_layout(
        plot_bgcolor='#666666',  # Fondo negro
        paper_bgcolor='#666666',  # Fondo del papel negro
        font=dict(color='white'),  # Texto en blanco
        title=dict(
            font=dict(size=26),  # Tamaño del título
            x=0.5  # Centrar el título
        ),
        xaxis_title='Fecha',  # Título del eje X
        yaxis_title='Valor de Humedad',  # Título del eje Y
        xaxis=dict(gridcolor='gray'),  # Cambiar el color de la cuadrícula en el eje X
        yaxis=dict(gridcolor='gray'),  # Cambiar el color de la cuadrícula en el eje Y

    )
    # Obtener el código HTML del gráfico
    divh = figh.to_html()

    #--------------------------------------------------------------------------------------------------------

    # Obtener los registrost de humedad
    registrost = RegistroTemperatura.objects.all()

    # Crear el DataFrame a partir de los registrost
    data_framet = pd.DataFrame(list(registrost.values('fecha', 'valor_temperatura')))

    
    # Crear el gráfico de línea con estilos personalizados
    figt = px.line(
        data_framet,
        x='fecha',
        y='valor_temperatura',
        title='Registros de Temperatura Históricos',  # Cambia el título
        labels={'fecha': 'Fecha', 'valor_humedad': 'Valor de temperatura'},  # Etiquetas personalizadas
    )

    # Personalizar el estilo del gráfico
    figt.update_traces(line=dict(color='#61FF61', width=2))  # Cambia el color de la línea y el grosor

    # Configturar el diseño del gráfico
    figt.update_layout(
        plot_bgcolor='#666666',  # Fondo negro
        paper_bgcolor='#666666',  # Fondo del papel negro
        font=dict(color='white'),  # Texto en blanco
        title=dict(
            font=dict(size=26),  # Tamaño del título
            x=0.5  # Centrar el título
        ),
        xaxis_title='Fecha',  # Título del eje X
        yaxis_title='Valor de Temperatura',  # Título del eje Y
        xaxis=dict(gridcolor='gray'),  # Cambiar el color de la cuadrícula en el eje X
        yaxis=dict(gridcolor='gray'),  # Cambiar el color de la cuadrícula en el eje Y

    )
    # Obtener el código HTML del gráfico
    divt = figt.to_html()


    return render(request, 'registros_humedad_temperatura.html', {'graficohumedad': divh,'graficotemperatura': divt})

def lista_actas(request):
    actas = ActaRecepcion.objects.all().order_by('-fecha')
    return render(request, 'lista_actas.html', {'actas': actas})

def detalle_acta(request, acta_id):
    acta = get_object_or_404(ActaRecepcion, pk=acta_id)
    recepciones = acta.recepcion_medicamentos.all()
    return render(request, 'detalle_acta.html', {'acta': acta, 'recepciones': recepciones})

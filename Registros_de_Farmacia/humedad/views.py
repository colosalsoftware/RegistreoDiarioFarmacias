from django.shortcuts import render
from .models import RegistroHumedad
import plotly.express as px
from plotly.offline import plot
import pandas as pd

def registros_humedad(request):
    # Obtener los registros de humedad
    registros = RegistroHumedad.objects.all()

    # Crear el DataFrame a partir de los registros
    data_frame = pd.DataFrame(list(registros.values('fecha', 'valor_humedad')))

    
    # Crear el gráfico de línea con estilos personalizados
    fig = px.line(
        data_frame,
        x='fecha',
        y='valor_humedad',
        title='Registros de Humedad Históricos',  # Cambia el título
        labels={'fecha': 'Fecha', 'valor_humedad': 'Valor de Humedad'},  # Etiquetas personalizadas
    )

    # Personalizar el estilo del gráfico
    fig.update_traces(line=dict(color='blue', width=4))  # Cambia el color de la línea y el grosor

    # Configurar el diseño del gráfico
    fig.update_layout(
        plot_bgcolor='black',  # Fondo negro
        paper_bgcolor='black',  # Fondo del papel negro
        font=dict(color='white'),  # Texto en blanco
        title=dict(
            font=dict(size=20),  # Tamaño del título
            x=0.5  # Centrar el título
        ),
        xaxis_title='Fecha',  # Título del eje X
        yaxis_title='Valor de Humedad',  # Título del eje Y
        xaxis=dict(gridcolor='gray'),  # Cambiar el color de la cuadrícula en el eje X
        yaxis=dict(gridcolor='gray'),  # Cambiar el color de la cuadrícula en el eje Y

    )
    # Obtener el código HTML del gráfico
    div = fig.to_html()

    return render(request, 'registros_humedad.html', {'grafico': div})

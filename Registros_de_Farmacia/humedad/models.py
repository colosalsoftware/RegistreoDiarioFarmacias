from django.db import models

class RegistroHumedad(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    valor_humedad = models.FloatField()  # Puedes ajustar este campo según tus necesidades

    def __str__(self):
        return f'Registro de Humedad - {self.fecha}'

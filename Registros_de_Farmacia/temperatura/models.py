from django.db import models

class RegistroTemperatura(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    valor_temperatura = models.FloatField()  # Puedes ajustar este campo según tus necesidades

    def __str__(self):
        return f'Registro de Temperatura - {self.fecha}'
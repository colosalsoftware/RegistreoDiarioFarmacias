from django.db import models

class Deposito(models.Model):
    nombre_Deposito = models.CharField(unique=True, max_length=255)
    def __str__(self):
        return self.nombre_Deposito
    
class Medicamento(models.Model):
    nombre_Medicamento = models.CharField(unique=True, max_length=255)
    def __str__(self):
        return self.nombre_Medicamento
    
class Laboratorio(models.Model):
    nombre_Laboratorio = models.CharField(unique=True, max_length=255)
    def __str__(self):
        return self.nombre_Laboratorio

class Firma(models.Model):
    nombre = models.CharField(unique=True, max_length=255)
    imagen = models.ImageField(upload_to='firma_imagenes/')
    def __str__(self):
        return self.nombre

class RecepcionMedicamento(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    registro_invima = models.TextField()
    lote = models.TextField()
    cantidad = models.IntegerField()
    fecha_vencimiento = models.DateField()
    cumple_norma = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.medicamento} - Lote {self.lote}"
    
class ActaRecepcion(models.Model):
    fecha = models.DateField()
    deposito = models.ForeignKey(Deposito, on_delete=models.CASCADE)
    factura = models.TextField()
    recepcion_medicamentos = models.ManyToManyField(RecepcionMedicamento)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE)
    def __str__(self):
        return f"Acta de Recepción - {self.fecha}"

from django.db import models
from comprobantes.funciones_auxiliares import generar_ruta_comprobante
from gastos.models import GastoNoProgramado

class TipoComprobante(models.Model):
    nombre=models.CharField(max_length=64)
    descripcion=models.TextField(null=True, blank=True)
    class Meta:
        db_table='tipo_comprobante'
    def __str__(self):
        return self.nombre

class Comprobante(models.Model):
    gasto_no_programado=models.ForeignKey(GastoNoProgramado, on_delete=models.CASCADE)
    tipo_comprobante=models.ForeignKey(TipoComprobante, on_delete=models.PROTECT)
    fecha_hora_emision=models.DateTimeField()
    observaciones=models.TextField(null=True, blank=True)
    archivo=models.FileField(upload_to=generar_ruta_comprobante)
    class Meta:
        db_table='comprobante'
    def __str__(self):
        return f"({self.id}) ({self.tipo_comprobante.nombre}) {self.archivo}"
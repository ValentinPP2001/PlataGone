from django.db import models
from compras.models import Compra


class CategoriaGasto(models.Model):
    nombre = models.CharField(max_length=64)
    icono = models.ImageField(upload_to='categoria_gasto/iconos/', null=True, blank=True)
    class Meta:
        db_table = 'categoria_gasto'
    def __str__(self):
        return self.nombre


# TABLA PADRE
class Gasto(models.Model):
    concepto = models.CharField(max_length=124)
    categoria_gasto = models.ForeignKey(CategoriaGasto, on_delete=models.PROTECT)
    compra = models.ForeignKey(Compra, on_delete=models.PROTECT, null=True, blank=True)
    fecha_hora = models.DateTimeField()
    class Meta:
        db_table = 'gasto'
    def __str__(self):
        compra_info = f"Compra #{self.compra_id}" if self.compra_id else "Sin compra"
        return f"({self.id}) ({self.fecha_hora}) ({self.categoria_gasto.nombre}) {compra_info} - {self.concepto}"

# TABLAS HIJAS (Especializaciones)
class GastoNoProgramado(Gasto):
    monto = models.DecimalField(max_digits=16, decimal_places=2)
    class Meta:
        db_table = 'gasto_no_programado'
    def __str__(self):
        return f"({self.id}) {self.concepto} - ${self.monto}"


class GastoProgramado(Gasto):
    monto_estimado = models.DecimalField(max_digits=16, decimal_places=2)
    fecha_vencimiento = models.DateField()
    activo = models.BooleanField(default=False)
    class Meta:
        db_table = 'gasto_programado'
    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"({self.id}) {self.concepto} ({estado}) - Vence: {self.fecha_vencimiento}"
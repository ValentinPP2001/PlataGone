from django.db import models
from gastos.models import Gasto

# ==========================================
# 1. TABLA PADRE (Generalización)
# ==========================================
class Tarjeta(models.Model):
    nombre = models.CharField(max_length=100)
    entidad_emisora = models.CharField(max_length=100)
    ultimos_4_digitos = models.CharField(max_length=4)
    activa = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'tarjeta'
        
    def __str__(self):
        return f"{self.nombre} (**** {self.ultimos_4_digitos})"

# ==========================================
# 2. ESPECIALIZACIONES (Herencia Directa)
# ==========================================
class TarjetaDebito(Tarjeta):
    banco_asociado = models.CharField(max_length=100)
    class Meta:
        db_table = 'tarjeta_debito'

class TarjetaCredito(Tarjeta):
    limite_credito = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_cierre = models.DateField()
    fecha_vencimiento = models.DateField()
    
    class Meta:
        db_table = 'tarjeta_credito'

# ==========================================
# 3. RESUMEN DE TARJETA DE CRÉDITO
# ==========================================
class ResumenTarjetaCredito(models.Model):
    fecha_cierre = models.DateField()
    fecha_vencimiento = models.DateField()
    monto_total = models.DecimalField(max_digits=12, decimal_places=2)
    pagado = models.BooleanField(default=False)
    archivo = models.FileField(upload_to='tarjetas/resumenes/', null=True, blank=True)

    class Meta:
        db_table = 'resumen_tarjeta_credito'

    def __str__(self):
        return f"Resumen {self.fecha_cierre} - Total: ${self.monto_total}"


# ==========================================
# 4. CONSUMO DE TARJETA DE CRÉDITO
# ==========================================
class ConsumoTarjetaCredito(models.Model):
    tarjeta_credito = models.ForeignKey(TarjetaCredito, on_delete=models.PROTECT)
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)
    resumen_tarjeta = models.ForeignKey(ResumenTarjetaCredito, on_delete=models.SET_NULL, null=True, blank=True)
    cuota_actual = models.IntegerField(default=1)
    cuotas_totales = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'consumo_tarjeta_credito'
        
    def __str__(self):
        return f"Consumo Gasto #{self.gasto_id} - Cuota {self.cuota_actual}/{self.cuotas_totales}"
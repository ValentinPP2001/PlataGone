from django.db import models
from gastos.models import Gasto
from finanzas.models import Cuota, Ingreso
from tarjetas.models import ResumenTarjetaCredito, Tarjeta


# ==========================================
# 1. TABLAS CATÁLOGO / PARÁMETROS
# ==========================================
class TipoMovimiento(models.Model):
    nombre = models.CharField(max_length=64)

    class Meta:
        db_table = 'tipo_movimiento'

    def __str__(self):
        return self.nombre


class MedioDePago(models.Model):
    nombre = models.CharField(max_length=64)

    class Meta:
        db_table = 'medio_de_pago'

    def __str__(self):
        return self.nombre


# ==========================================
# 2. MOVIMIENTO PRINCIPAL
# ==========================================
class Movimiento(models.Model):
    monto = models.DecimalField(max_digits=16, decimal_places=2)
    fecha = models.DateField()
    tipo_de_movimiento = models.ForeignKey(TipoMovimiento, on_delete=models.PROTECT)
    medio_de_pago = models.ForeignKey(MedioDePago, on_delete=models.PROTECT)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'movimiento'

    def __str__(self):
        return f"Movimiento #{self.id} ({self.tipo_de_movimiento.nombre}) - ${self.monto}"


# ==========================================
# 3. APLICACIÓN DE INGRESOS
# ==========================================
class IngresoAplicado(models.Model):
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE)
    ingreso = models.ForeignKey(Ingreso, on_delete=models.PROTECT)

    class Meta:
        db_table = 'ingreso_aplicado'

    def __str__(self):
        return f"IngresoAplicado #{self.id} (Ingreso #{self.ingreso_id} -> Movimiento #{self.movimiento_id})"


# ==========================================
# 4. APLICACIÓN DE PAGOS (HERENCIA)
# ==========================================
class PagoAplicado(models.Model):
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pago_aplicado'

    def __str__(self):
        return f"PagoAplicado #{self.id} (Movimiento #{self.movimiento_id})"


class PagoAplicadoGasto(PagoAplicado):
    gasto = models.ForeignKey(Gasto, on_delete=models.PROTECT)

    class Meta:
        db_table = 'pago_aplicado_gasto'


class PagoAplicadoCuota(PagoAplicado):
    cuota = models.ForeignKey(Cuota, on_delete=models.PROTECT)

    class Meta:
        db_table = 'pago_aplicado_cuota'


class PagoAplicadoResumenTarjeta(PagoAplicado):
    resumen_tarjeta = models.ForeignKey(ResumenTarjetaCredito, on_delete=models.PROTECT)

    class Meta:
        db_table = 'pago_aplicado_resumen_tarjeta'
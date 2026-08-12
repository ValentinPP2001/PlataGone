from django.db import models


# ==========================================
# 1. TABLAS CATÁLOGO / PARÁMETROS
# ==========================================
class TipoIngreso(models.Model):
    nombre = models.CharField(max_length=64)

    class Meta:
        db_table = 'tipo_ingreso'
        
    def __str__(self):
        return self.nombre


class FuenteIngreso(models.Model):
    nombre = models.CharField(max_length=64)

    class Meta:
        db_table = 'fuente_ingreso'

    def __str__(self):
        return self.nombre


class EstadoDeuda(models.Model):
    nombre = models.CharField(max_length=64)

    class Meta:
        db_table = 'estado_deuda'

    def __str__(self):
        return self.nombre


class EntidadAcreedora(models.Model):
    nombre = models.CharField(max_length=120)

    class Meta:
        db_table = 'entidad_acreedora'

    def __str__(self):
        return self.nombre


# ==========================================
# 2. TRANSACCIONES PRINCIPALES
# ==========================================
class Ingreso(models.Model):
    concepto = models.CharField(max_length=120)
    monto = models.DecimalField(max_digits=16, decimal_places=2)
    fecha = models.DateField()
    tipo_ingreso = models.ForeignKey(TipoIngreso, on_delete=models.PROTECT)
    fuente_ingreso = models.ForeignKey(FuenteIngreso, on_delete=models.PROTECT)

    class Meta:
        db_table = 'ingreso'

    def __str__(self):
        return f"({self.fecha}) {self.concepto} - ${self.monto}"


class Deuda(models.Model):
    monto = models.DecimalField(max_digits=16, decimal_places=2)
    fecha_creacion = models.DateField()
    estado = models.ForeignKey(EstadoDeuda, on_delete=models.PROTECT)
    entidad_acreedora = models.ForeignKey(EntidadAcreedora, on_delete=models.PROTECT)

    class Meta:
        db_table = 'deuda'

    def __str__(self):
        return f"Deuda #{self.id} ({self.acreedor.nombre}) - ${self.monto}"


# ==========================================
# 3. PLANIFICACIÓN Y CUOTAS DE DEUDAS
# ==========================================
class PlanDePago(models.Model):
    fecha = models.DateField()
    deuda = models.ForeignKey(Deuda, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=16, decimal_places=2)
    cantidad_de_cuotas = models.IntegerField()
    vigente = models.BooleanField(default=True)

    class Meta:
        db_table = 'plan_de_pago'

    def __str__(self):
        return f"Plan Deuda #{self.deuda_id} - {self.cantidad_de_cuotas} cuotas"


class Cuota(models.Model):
    plan_de_pago = models.ForeignKey(PlanDePago, on_delete=models.CASCADE)
    monto_cuota = models.DecimalField(max_digits=16, decimal_places=2)
    fecha_vencimiento = models.DateField()
    pagada = models.BooleanField(default=False)

    class Meta:
        db_table = 'cuota'

    def __str__(self):
        estado = "Pagada" if self.pagada else "Pendiente"
        return f"Cuota #{self.id} (Plan #{self.plan_de_pago_id}) - ${self.monto_cuota} [{estado}]"
from django.contrib import admin
from finanzas.models import (
    TipoIngreso,
    FuenteIngreso,
    EstadoDeuda,
    EntidadAcreedora,
    Ingreso,
    Deuda,
    PlanDePago,
    Cuota,
)


# ==========================================
# 1. TABLAS CATÁLOGO / PARÁMETROS
# ==========================================
@admin.register(TipoIngreso)
class TipoIngresoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_editable = ['nombre']
    search_fields = ['nombre']
    list_per_page = 15


@admin.register(FuenteIngreso)
class FuenteIngresoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_editable = ['nombre']
    search_fields = ['nombre']
    list_per_page = 15


@admin.register(EstadoDeuda)
class EstadoDeudaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_editable = ['nombre']
    search_fields = ['nombre']
    list_per_page = 15


@admin.register(EntidadAcreedora)
class EntidadAcreedoraAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_editable = ['nombre']
    search_fields = ['nombre']
    list_per_page = 15


# ==========================================
# 2. TRANSACCIONES PRINCIPALES
# ==========================================
@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    list_display = ['id', 'concepto', 'monto', 'fecha', 'tipo_ingreso', 'fuente_ingreso']
    list_editable = ['monto', 'fecha', 'tipo_ingreso', 'fuente_ingreso']
    search_fields = ['concepto', 'tipo_ingreso__nombre', 'fuente_ingreso__nombre']
    list_filter = ['tipo_ingreso', 'fuente_ingreso', 'fecha']
    list_select_related = ['tipo_ingreso', 'fuente_ingreso']
    list_per_page = 15


@admin.register(Deuda)
class DeudaAdmin(admin.ModelAdmin):
    list_display = ['id', 'entidad_acreedora', 'monto', 'fecha_creacion', 'estado']
    list_editable = ['monto', 'fecha_creacion', 'estado']
    search_fields = ['entidad_acreedora__nombre']
    list_filter = ['estado', 'entidad_acreedora', 'fecha_creacion']
    list_select_related = ['estado', 'entidad_acreedora']
    list_per_page = 15


# ==========================================
# 3. PLANIFICACIÓN Y CUOTAS DE DEUDAS
# ==========================================
@admin.register(PlanDePago)
class PlanDePagoAdmin(admin.ModelAdmin):
    list_display = ['id', 'deuda', 'fecha', 'monto_total', 'cantidad_de_cuotas', 'vigente']
    list_editable = ['monto_total', 'cantidad_de_cuotas', 'vigente']
    search_fields = ['deuda__entidad_acreedora__nombre']
    list_filter = ['vigente', 'fecha']
    list_select_related = ['deuda', 'deuda__entidad_acreedora']
    list_per_page = 15


@admin.register(Cuota)
class CuotaAdmin(admin.ModelAdmin):
    list_display = ['id', 'plan_de_pago', 'monto_cuota', 'fecha_vencimiento', 'pagada']
    list_editable = ['monto_cuota', 'fecha_vencimiento', 'pagada']
    search_fields = ['plan_de_pago__deuda__entidad_acreedora__nombre']
    list_filter = ['pagada', 'fecha_vencimiento']
    list_select_related = ['plan_de_pago', 'plan_de_pago__deuda']
    list_per_page = 15
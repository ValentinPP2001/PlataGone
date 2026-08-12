from django.contrib import admin
from movimientos.models import (
    TipoMovimiento,
    MedioDePago,
    Movimiento,
    IngresoAplicado,
    PagoAplicado,
    PagoAplicadoGasto,
    PagoAplicadoCuota,
    PagoAplicadoResumenTarjeta,
)


# ==========================================
# 1. TABLAS CATÁLOGO / PARÁMETROS
# ==========================================
@admin.register(TipoMovimiento)
class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_editable = ['nombre']
    search_fields = ['nombre']
    list_per_page = 15


@admin.register(MedioDePago)
class MedioDePagoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_editable = ['nombre']
    search_fields = ['nombre']
    list_per_page = 15


# ==========================================
# 2. INLINES PARA APLICACIONES DENTRO DE MOVIMIENTO
# ==========================================
class IngresoAplicadoInline(admin.TabularInline):
    model = IngresoAplicado
    extra = 1
    autocomplete_fields = ['ingreso']


class PagoAplicadoGastoInline(admin.TabularInline):
    model = PagoAplicadoGasto
    extra = 1
    autocomplete_fields = ['gasto']


class PagoAplicadoCuotaInline(admin.TabularInline):
    model = PagoAplicadoCuota
    extra = 1
    autocomplete_fields = ['cuota']


class PagoAplicadoResumenTarjetaInline(admin.TabularInline):
    model = PagoAplicadoResumenTarjeta
    extra = 1
    autocomplete_fields = ['resumen_tarjeta']


# ==========================================
# 3. MOVIMIENTO PRINCIPAL
# ==========================================
@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'monto',
        'fecha',
        'tipo_de_movimiento',
        'medio_de_pago',
        'tarjeta',
    ]
    list_editable = ['monto', 'fecha', 'tipo_de_movimiento', 'medio_de_pago', 'tarjeta']
    search_fields = ['id', 'tarjeta__nombre']
    list_filter = ['tipo_de_movimiento', 'medio_de_pago', 'fecha', 'tarjeta']
    list_select_related = ['tipo_de_movimiento', 'medio_de_pago', 'tarjeta']
    inlines = [
        IngresoAplicadoInline,
        PagoAplicadoGastoInline,
        PagoAplicadoCuotaInline,
        PagoAplicadoResumenTarjetaInline,
    ]
    list_per_page = 15


# ==========================================
# 4. APLICACIÓN DE INGRESOS
# ==========================================
@admin.register(IngresoAplicado)
class IngresoAplicadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'movimiento', 'ingreso']
    search_fields = ['ingreso__concepto', 'movimiento__id']
    list_filter = ['movimiento__fecha']
    list_select_related = ['movimiento', 'ingreso']
    list_per_page = 15


# ==========================================
# 5. APLICACIÓN DE PAGOS
# ==========================================
@admin.register(PagoAplicado)
class PagoAplicadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'movimiento']
    search_fields = ['movimiento__id']
    list_select_related = ['movimiento']
    list_per_page = 15


@admin.register(PagoAplicadoGasto)
class PagoAplicadoGastoAdmin(admin.ModelAdmin):
    list_display = ['id', 'movimiento', 'gasto']
    search_fields = ['gasto__concepto', 'movimiento__id']
    list_select_related = ['movimiento', 'gasto']
    list_per_page = 15


@admin.register(PagoAplicadoCuota)
class PagoAplicadoCuotaAdmin(admin.ModelAdmin):
    list_display = ['id', 'movimiento', 'cuota']
    search_fields = ['cuota__id', 'movimiento__id']
    list_select_related = ['movimiento', 'cuota']
    list_per_page = 15


@admin.register(PagoAplicadoResumenTarjeta)
class PagoAplicadoResumenTarjetaAdmin(admin.ModelAdmin):
    list_display = ['id', 'movimiento', 'resumen_tarjeta']
    search_fields = ['resumen_tarjeta__id', 'movimiento__id']
    list_select_related = ['movimiento', 'resumen_tarjeta']
    list_per_page = 15
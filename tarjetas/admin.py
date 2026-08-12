from django.contrib import admin
from tarjetas.models import (
    Tarjeta,
    TarjetaDebito,
    TarjetaCredito,
    ResumenTarjetaCredito,
    ConsumoTarjetaCredito,
)


@admin.register(Tarjeta)
class TarjetaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'entidad_emisora', 'ultimos_4_digitos', 'activa']
    list_editable = ['activa']
    search_fields = ['nombre', 'entidad_emisora', 'ultimos_4_digitos']
    list_filter = ['activa', 'entidad_emisora']
    list_per_page = 15


@admin.register(TarjetaDebito)
class TarjetaDebitoAdmin(admin.ModelAdmin):
    # Hereda campos de Tarjeta más 'banco_asociado'
    list_display = ['id', 'nombre', 'entidad_emisora', 'banco_asociado', 'ultimos_4_digitos', 'activa']
    list_editable = ['activa']
    search_fields = ['nombre', 'entidad_emisora', 'banco_asociado', 'ultimos_4_digitos']
    list_filter = ['activa', 'banco_asociado']
    list_per_page = 15


@admin.register(TarjetaCredito)
class TarjetaCreditoAdmin(admin.ModelAdmin):
    # Hereda campos de Tarjeta más límite y fechas
    list_display = [
        'id',
        'nombre',
        'entidad_emisora',
        'limite_credito',
        'fecha_cierre',
        'fecha_vencimiento',
        'activa',
    ]
    list_editable = ['limite_credito', 'fecha_cierre', 'fecha_vencimiento', 'activa']
    search_fields = ['nombre', 'entidad_emisora', 'ultimos_4_digitos']
    list_filter = ['activa', 'fecha_cierre', 'fecha_vencimiento']
    list_per_page = 15


@admin.register(ResumenTarjetaCredito)
class ResumenTarjetaCreditoAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_cierre', 'fecha_vencimiento', 'monto_total', 'pagado', 'archivo']
    list_editable = ['pagado', 'monto_total', 'fecha_cierre', 'fecha_vencimiento']
    list_filter = ['pagado', 'fecha_cierre', 'fecha_vencimiento']
    search_fields = ['monto_total']
    list_per_page = 15


@admin.register(ConsumoTarjetaCredito)
class ConsumoTarjetaCreditoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'gasto',
        'tarjeta_credito',
        'cuotas_info',
        'resumen_tarjeta',
    ]
    list_editable = ['resumen_tarjeta']
    search_fields = ['gasto__concepto', 'tarjeta_credito__nombre']
    list_filter = ['tarjeta_credito', 'resumen_tarjeta']
    list_select_related = ['gasto', 'tarjeta_credito', 'resumen_tarjeta']  # Optimiza las consultas SQL
    list_per_page = 15

    # Método para mostrar la relación de cuotas de forma legible (ej: "1 / 12")
    @admin.display(description='Cuotas')
    def cuotas_info(self, obj):
        return f"{obj.cuota_actual} / {obj.cuotas_totales}"
from django.contrib import admin
from comprobantes.models import TipoComprobante, Comprobante

@admin.register(TipoComprobante)
class TipoComprobanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion']
    list_editable = ['nombre']
    search_fields = ['nombre']
    list_per_page = 15
    
@admin.register(Comprobante)
class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_hora_emision', 'tipo_comprobante', 'gasto_no_programado', 'observaciones', 'archivo']
    list_editable = ['fecha_hora_emision', 'tipo_comprobante']
    search_fields = ['fecha_hora_emision', 'tipo_comprobante']
    list_per_page = 15
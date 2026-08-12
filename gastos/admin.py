from django.contrib import admin
from gastos.models import CategoriaGasto, Gasto, GastoNoProgramado, GastoProgramado

@admin.register(CategoriaGasto)
class CategoriaGastoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'icono']
    list_editable = ['nombre', 'icono']
    search_fields = ['nombre']
    list_per_page = 15
    
@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_hora', 'concepto', 'categoria_gasto', 'compra']
    list_editable = ['fecha_hora', 'concepto', 'categoria_gasto', 'compra']
    search_fields = ['fecha_hora', 'concepto', 'categoria_gasto', 'compra__id']
    list_per_page = 15

@admin.register(GastoNoProgramado)
class GastoNoProgramadoAdmin(admin.ModelAdmin):
    list_display = ['id','gasto','monto']
    list_editable = ['gasto','monto']
    search_fields = ['gasto__concepto']
    list_per_page = 15
    
@admin.register(GastoProgramado)
class GastoProgramadoAdmin(admin.ModelAdmin):
    list_display = ['id','gasto','activo','fecha_vencimiento','monto_estimado']
    list_editable = ['activo','fecha_vencimiento','monto_estimado']
    search_fields = ['gasto__concepto']
    list_filter = ['activo']
    list_per_page = 15
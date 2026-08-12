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
    search_fields = ['concepto', 'categoria_gasto__nombre']
    list_per_page = 15


@admin.register(GastoNoProgramado)
class GastoNoProgramadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'concepto', 'monto', 'categoria_gasto', 'fecha_hora']
    list_editable = ['monto']
    search_fields = ['concepto', 'categoria_gasto__nombre']
    list_per_page = 15


@admin.register(GastoProgramado)
class GastoProgramadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'concepto', 'monto_estimado', 'fecha_vencimiento', 'activo', 'categoria_gasto']
    list_editable = ['monto_estimado', 'fecha_vencimiento', 'activo']
    search_fields = ['concepto', 'categoria_gasto__nombre']
    list_filter = ['activo']
    list_per_page = 15
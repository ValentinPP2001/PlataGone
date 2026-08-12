from django.contrib import admin
from compras.models import (
    UnidadMedida,
    CategoriaProducto,
    Producto,
    Rubro,
    Comercio,
    Compra,
    CompraProducto
)

@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'abreviatura', 'descripcion']
    list_editable = ['abreviatura', 'nombre']
    search_fields = ['nombre', 'abreviatura']
    list_per_page = 15
    
@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion']
    list_editable = ['nombre']
    search_fields = ['nombre']
    list_per_page = 15
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'categoria', 'unidad_medida']
    list_editable = ['nombre', 'categoria', 'unidad_medida']
    search_fields = ['nombre', 'categoria', 'unidad_medida']
    list_per_page = 15
    
@admin.register(Rubro)
class RubroAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion']
    list_editable = ['nombre']
    search_fields = ['nombre']
    list_per_page = 15
    
@admin.register(Comercio)
class ComercioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'direccion', 'get_rubros']
    list_editable = ['nombre', 'direccion']
    search_fields = ['nombre']
    list_per_page = 15
    
    filter_horizontal = ('rubros',)
    
    @admin.display(description='Rubros')
    def get_rubros(self, obj):
        # Une los nombres de los rubros separados por comas
        return ", ".join([rubro.nombre for rubro in obj.rubros.all()])
    
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_hora', 'comercio__nombre', 'total']
    search_fields = ['comercio__nombre']
    list_per_page = 15
    
@admin.register(CompraProducto)
class CompraProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'compra__id', 'compra__fecha_hora', 'producto__nombre', 'cantidad', 'precio_unitario', 'subtotal']
    search_fields = ['compra__comercio__nombre', 'producto__nombre']
    list_per_page = 15
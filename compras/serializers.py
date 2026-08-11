from rest_framework import serializers
from compras.models import (
    UnidadMedida,
    CategoriaProducto,
    Producto,
    Rubro,
    Comercio,
    Compra,
    CompraProducto
)

class UnidadMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadMedida
        fields = ['id', 'nombre', 'descripcion']

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = ['id', 'nombre', 'descripcion']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'categoria', 'unidad_medida']

class RubroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubro
        fields = ['id', 'nombre', 'descripcion']

class ComercioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comercio
        fields = ['id', 'nombre', 'direccion', 'rubros']

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['id', 'fecha_hora', 'comercio', 'total']

class CompraProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraProducto
        fields = ['id', 'producto', 'compra', 'cantidad', 'precio_unitario', 'subtotal']

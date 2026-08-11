from rest_framework import viewsets, mixins
from compras.models import (
    UnidadMedida,
    CategoriaProducto,
    Producto,
    Rubro,
    Comercio,
    Compra,
    CompraProducto
)
from compras.serializers import (
    UnidadMedidaSerializer,
    CategoriaProductoSerializer,
    ProductoSerializer,
    RubroSerializer,
    ComercioSerializer,
    CompraSerializer,
    CompraProductoSerializer
)

class UnidadMedidaReadView(viewsets.ReadOnlyModelViewSet):
    queryset = UnidadMedida.objects.all()
    serializer_class = UnidadMedidaSerializer

class CategoriaProductoView(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class RubroReadView(viewsets.ReadOnlyModelViewSet):
    queryset = Rubro.objects.all()
    serializer_class = RubroSerializer

class ComercioView(viewsets.ModelViewSet):
    queryset = Comercio.objects.all()
    serializer_class = ComercioSerializer

class CompraView(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class CompraProductoView(
    viewsets.GenericViewSet, 
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin,
    mixins.ListModelMixin
    ):
    queryset = CompraProducto.objects.all()
    serializer_class = CompraProductoSerializer
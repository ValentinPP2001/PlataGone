from django.urls import path, include
from rest_framework.routers import DefaultRouter
from compras.views import (
    UnidadMedidaReadView,
    CategoriaProductoView,
    ProductoView,
    RubroReadView,
    ComercioView,
    CompraView,
    CompraProductoView
)

router = DefaultRouter()

router.register(r'unidad-medida', UnidadMedidaReadView, basename='unidad-medida')
router.register(r'categoria-producto', CategoriaProductoView, basename='categoria-producto')
router.register(r'producto', ProductoView, basename='producto')
router.register(r'rubro', RubroReadView, basename='rubro')
router.register(r'comercio', ComercioView, basename='comercio')
router.register(r'compra', CompraView, basename='compra')
router.register(r'compra-producto', CompraProductoView, basename='compra-producto')

urlpatterns = [
    path('', include(router.urls)),
]
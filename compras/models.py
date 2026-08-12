from django.db import models

class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'unidad_medida'

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'categoria_producto'

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.PROTECT)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)
    class Meta:
        db_table = 'producto'

class Rubro(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'rubro'

class Comercio(models.Model):
    nombre = models.CharField(max_length=64)
    direccion = models.TextField(null=True, blank=True)
    rubros = models.ManyToManyField(Rubro)
    class Meta:
        db_table = 'comercio'

class Compra(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    comercio = models.ForeignKey(Comercio, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=16, decimal_places=2)
    class Meta:
        db_table = 'compra'

class CompraProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    compra = models.ForeignKey(Compra, on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=16, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=16, decimal_places=2)
    subtotal = models.DecimalField(max_digits=16, decimal_places=2)
    class Meta:
        db_table = 'compra_producto'
import uuid
from django.db import models


class TipoMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=15)
    descripcion = models.TextField()
    duracion_estimada_horas = models.IntegerField()
    periodicidad_km = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"


class OrdenMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_orden = models.CharField(max_length=20, unique=True)
    placa_bus = models.CharField(max_length=10)
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.PROTECT, related_name='ordenes')
    tecnico_responsable = models.CharField(max_length=100)
    fecha_programada = models.DateField()
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    kilometraje_bus = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=15)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"OM-{self.numero_orden} | Bus {self.placa_bus} | {self.estado}"


class Repuesto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    stock_actual = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=5)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.codigo} - {self.nombre} (stock: {self.stock_actual})"


class DetalleMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orden = models.ForeignKey(OrdenMantenimiento, on_delete=models.CASCADE, related_name='detalles')
    repuesto = models.ForeignKey(Repuesto, on_delete=models.PROTECT, related_name='usos')
    cantidad_usada = models.IntegerField()
    precio_unitario_momento = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.repuesto.nombre} x{self.cantidad_usada} - OM {self.orden.numero_orden}"                                      
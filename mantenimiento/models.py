import uuid
from django.db import models

CATEGORIAS_MANT = [
    ('preventivo', 'Preventivo'),
    ('correctivo', 'Correctivo'),
    ('predictivo', 'Predictivo'),
    ('emergencia', 'Emergencia'),
]

ESTADOS_ORDEN = [
    ('programada', 'Programada'),
    ('en_proceso', 'En Proceso'),
    ('completada', 'Completada'),
    ('cancelada', 'Cancelada'),
]


class TipoMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    categoria = models.CharField(max_length=15, choices=CATEGORIAS_MANT, verbose_name='Categoría')
    descripcion = models.TextField(verbose_name='Descripción')
    duracion_estimada_horas = models.IntegerField(verbose_name='Duración Estimada (h)')
    periodicidad_km = models.IntegerField(null=True, blank=True, verbose_name='Periodicidad (km)')

    class Meta:
        verbose_name = 'Tipo de Mantenimiento'
        verbose_name_plural = 'Tipos de Mantenimiento'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"


class OrdenMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_orden = models.CharField(max_length=20, unique=True, verbose_name='N° Orden')
    placa_bus = models.CharField(max_length=10, verbose_name='Placa del Bus')
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.PROTECT, related_name='ordenes', verbose_name='Tipo')
    tecnico_responsable = models.CharField(max_length=100, verbose_name='Técnico Responsable')
    fecha_programada = models.DateField(verbose_name='Fecha Programada')
    fecha_inicio = models.DateTimeField(null=True, blank=True, verbose_name='Fecha Inicio')
    fecha_fin = models.DateTimeField(null=True, blank=True, verbose_name='Fecha Fin')
    kilometraje_bus = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Kilometraje Bus')
    estado = models.CharField(max_length=15, choices=ESTADOS_ORDEN, default='programada', verbose_name='Estado')
    observaciones = models.TextField(blank=True, verbose_name='Observaciones')

    class Meta:
        verbose_name = 'Orden de Mantenimiento'
        verbose_name_plural = 'Órdenes de Mantenimiento'
        ordering = ['-fecha_programada']

    def __str__(self):
        return f"OM-{self.numero_orden} | Bus {self.placa_bus} | {self.get_estado_display()}"

    @property
    def costo_total(self):
        return sum(d.cantidad_usada * d.precio_unitario_momento for d in self.detalles.all())

    def get_estado_badge(self):
        colores = {
            'programada': 'info',
            'en_proceso': 'warning',
            'completada': 'success',
            'cancelada': 'danger',
        }
        return colores.get(self.estado, 'secondary')


class Repuesto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    stock_actual = models.IntegerField(default=0, verbose_name='Stock Actual')
    stock_minimo = models.IntegerField(default=5, verbose_name='Stock Mínimo')
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Precio Unitario')

    class Meta:
        verbose_name = 'Repuesto'
        verbose_name_plural = 'Repuestos'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} — {self.nombre}"

    @property
    def bajo_stock(self):
        return self.stock_actual <= self.stock_minimo


class DetalleMantenimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orden = models.ForeignKey(OrdenMantenimiento, on_delete=models.CASCADE, related_name='detalles', verbose_name='Orden')
    repuesto = models.ForeignKey(Repuesto, on_delete=models.PROTECT, related_name='usos', verbose_name='Repuesto')
    cantidad_usada = models.IntegerField(verbose_name='Cantidad')
    precio_unitario_momento = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Precio Unit.')

    class Meta:
        verbose_name = 'Detalle de Mantenimiento'
        verbose_name_plural = 'Detalles de Mantenimiento'

    def __str__(self):
        return f"{self.repuesto.nombre} x{self.cantidad_usada}"

    @property
    def subtotal(self):
        return self.cantidad_usada * self.precio_unitario_momento

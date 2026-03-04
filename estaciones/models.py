import uuid
from django.db import models


class Estacion(models.Model):
    TIPO_CHOICES = [
        ('sencilla', 'Sencilla'),
        ('cabecera', 'Cabecera'),
        ('intermedia', 'Intermedia'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    localidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    tiene_biciparqueo = models.BooleanField(default=False)
    tiene_ascensor = models.BooleanField(default=False)
    en_operacion = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class TaquillaCarga(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='taquillas')
    numero = models.IntegerField()
    operativa = models.BooleanField(default=True)
    ultima_revision = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Taquilla #{self.numero} - {self.estacion.nombre}"


class IncidenciaEstacion(models.Model):
    TIPO_CHOICES = [
        ('vandalismo', 'Vandalismo'),
        ('falla_tecnica', 'Falla Técnica'),
        ('emergencia', 'Emergencia'),
        ('mantenimiento', 'Mantenimiento Preventivo'),
    ]
    ESTADO_CHOICES = [
        ('abierta', 'Abierta'),
        ('en_proceso', 'En Proceso'),
        ('resuelta', 'Resuelta'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='incidencias')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='abierta')

    def __str__(self):
        return f"{self.tipo} - {self.estacion.nombre} ({self.estado})"
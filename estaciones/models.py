import uuid
from django.db import models

TIPOS_ESTACION = [
    ('portal', 'Portal'),
    ('troncal', 'Troncal'),
    ('intermedia', 'Intermedia'),
    ('sencilla', 'Sencilla'),
]

TIPOS_INCIDENCIA = [
    ('infraestructura', 'Infraestructura'),
    ('seguridad', 'Seguridad'),
    ('tecnica', 'Técnica'),
    ('servicio', 'Servicio'),
    ('otra', 'Otra'),
]

ESTADOS_INCIDENCIA = [
    ('abierta', 'Abierta'),
    ('en_proceso', 'En Proceso'),
    ('resuelta', 'Resuelta'),
    ('cerrada', 'Cerrada'),
]


class Estacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=10, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    tipo = models.CharField(max_length=15, choices=TIPOS_ESTACION, verbose_name='Tipo')
    localidad = models.CharField(max_length=100, verbose_name='Localidad')
    direccion = models.CharField(max_length=200, verbose_name='Dirección')
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Latitud')
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Longitud')
    tiene_biciparqueo = models.BooleanField(default=False, verbose_name='Biciparqueo')
    tiene_ascensor = models.BooleanField(default=False, verbose_name='Ascensor')
    en_operacion = models.BooleanField(default=True, verbose_name='En Operación')

    class Meta:
        verbose_name = 'Estación'
        verbose_name_plural = 'Estaciones'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} — {self.nombre}"

    @property
    def total_taquillas(self):
        return self.taquillas.count()

    @property
    def taquillas_operativas(self):
        return self.taquillas.filter(operativa=True).count()

    @property
    def incidencias_abiertas(self):
        return self.incidencias.filter(estado='abierta').count()


class TaquillaCarga(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='taquillas', verbose_name='Estación')
    numero = models.IntegerField(verbose_name='Número')
    operativa = models.BooleanField(default=True, verbose_name='Operativa')
    ultima_revision = models.DateField(null=True, blank=True, verbose_name='Última Revisión')

    class Meta:
        verbose_name = 'Taquilla de Carga'
        verbose_name_plural = 'Taquillas de Carga'
        ordering = ['estacion', 'numero']

    def __str__(self):
        return f"Taquilla #{self.numero} — {self.estacion.nombre}"


class IncidenciaEstacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='incidencias', verbose_name='Estación')
    tipo = models.CharField(max_length=20, choices=TIPOS_INCIDENCIA, verbose_name='Tipo')
    descripcion = models.TextField(verbose_name='Descripción')
    fecha_reporte = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Reporte')
    fecha_resolucion = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Resolución')
    estado = models.CharField(max_length=15, choices=ESTADOS_INCIDENCIA, default='abierta', verbose_name='Estado')

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'
        ordering = ['-fecha_reporte']

    def __str__(self):
        return f"{self.get_tipo_display()} — {self.estacion.nombre} ({self.get_estado_display()})"

    @property
    def resuelta(self):
        return self.estado in ['resuelta', 'cerrada']

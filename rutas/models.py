import uuid
from django.db import models

TIPOS_RUTA = [
    ('troncal', 'Troncal'),
    ('alimentadora', 'Alimentadora'),
    ('express', 'Express'),
    ('complementaria', 'Complementaria'),
    ('dual', 'Dual'),
]

DIAS_OPCIONES = [
    ('L-V', 'Lunes a Viernes'),
    ('L-S', 'Lunes a Sábado'),
    ('L-D', 'Lunes a Domingo'),
    ('S-D', 'Sábados y Domingos'),
    ('fes', 'Festivos'),
]


class Portal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    ubicacion = models.CharField(max_length=200, verbose_name='Ubicación')
    localidad = models.CharField(max_length=100, verbose_name='Localidad')
    capacidad_buses = models.IntegerField(verbose_name='Capacidad de Buses')
    activo = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        verbose_name = 'Portal'
        verbose_name_plural = 'Portales'
        ordering = ['nombre']

    def __str__(self):
        return f"Portal {self.nombre}"

    @property
    def total_rutas(self):
        return self.rutas_origen.count() + self.rutas_destino.count()


class Ruta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=10, unique=True, verbose_name='Código')
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    tipo = models.CharField(max_length=20, choices=TIPOS_RUTA, verbose_name='Tipo')
    portal_origen = models.ForeignKey(Portal, on_delete=models.PROTECT, related_name='rutas_origen', verbose_name='Portal Origen')
    portal_destino = models.ForeignKey(Portal, on_delete=models.PROTECT, related_name='rutas_destino', verbose_name='Portal Destino')
    distancia_km = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Distancia (km)')
    tiempo_estimado_min = models.IntegerField(verbose_name='Tiempo Estimado (min)')
    frecuencia_min = models.IntegerField(verbose_name='Frecuencia (min)')
    activa = models.BooleanField(default=True, verbose_name='Activa')

    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'
        ordering = ['codigo']

    def __str__(self):
        return f"Ruta {self.codigo} — {self.nombre}"

    @property
    def descripcion_corta(self):
        return f"{self.portal_origen.nombre} → {self.portal_destino.nombre}"


class HorarioRuta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='horarios', verbose_name='Ruta')
    dias = models.CharField(max_length=20, choices=DIAS_OPCIONES, verbose_name='Días')
    hora_inicio = models.TimeField(verbose_name='Hora Inicio')
    hora_fin = models.TimeField(verbose_name='Hora Fin')

    class Meta:
        verbose_name = 'Horario de Ruta'
        verbose_name_plural = 'Horarios de Ruta'

    def __str__(self):
        return f"{self.ruta.codigo} — {self.get_dias_display()}: {self.hora_inicio.strftime('%H:%M')}-{self.hora_fin.strftime('%H:%M')}"

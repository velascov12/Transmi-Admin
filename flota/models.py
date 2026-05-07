import uuid
from django.db import models


ESTADOS_BUS = [
    ('activo', 'Activo'),
    ('mantenimiento', 'En Mantenimiento'),
    ('inactivo', 'Inactivo'),
    ('baja', 'Dado de Baja'),
]

TURNOS = [
    ('mañana', 'Mañana'),
    ('tarde', 'Tarde'),
    ('noche', 'Noche'),
    ('doble', 'Doble Turno'),
]


class TipoBus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    capacidad_pasajeros = models.IntegerField(verbose_name='Capacidad de Pasajeros')
    longitud_metros = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Longitud (m)')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Tipo de Bus'
        verbose_name_plural = 'Tipos de Bus'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} (cap. {self.capacidad_pasajeros})"

    @property
    def total_buses(self):
        return self.buses.count()


class Bus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    placa = models.CharField(max_length=10, unique=True, verbose_name='Placa')
    numero_interno = models.CharField(max_length=10, unique=True, verbose_name='N° Interno')
    tipo = models.ForeignKey(TipoBus, on_delete=models.PROTECT, related_name='buses', verbose_name='Tipo de Bus')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    anio_fabricacion = models.IntegerField(verbose_name='Año de Fabricación')
    kilometraje = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Kilometraje')
    estado = models.CharField(max_length=20, choices=ESTADOS_BUS, default='activo', verbose_name='Estado')
    fecha_ingreso = models.DateField(verbose_name='Fecha de Ingreso')

    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'
        ordering = ['numero_interno']

    def __str__(self):
        return f"Bus {self.numero_interno} - {self.placa}"

    @property
    def esta_activo(self):
        return self.estado == 'activo'

    @property
    def tiene_conductor(self):
        return hasattr(self, 'conductor') and self.conductor is not None

    def get_estado_badge(self):
        colores = {
            'activo': 'success',
            'mantenimiento': 'warning',
            'inactivo': 'secondary',
            'baja': 'danger',
        }
        return colores.get(self.estado, 'secondary')


class Conductor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cedula = models.CharField(max_length=15, unique=True, verbose_name='Cédula')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    licencia = models.CharField(max_length=20, unique=True, verbose_name='N° Licencia')
    turno = models.CharField(max_length=10, choices=TURNOS, verbose_name='Turno')
    bus_asignado = models.OneToOneField(
        Bus, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='conductor', verbose_name='Bus Asignado'
    )
    activo = models.BooleanField(default=True, verbose_name='Activo')
    fecha_contratacion = models.DateField(verbose_name='Fecha de Contratación')
    telefono = models.CharField(max_length=15, blank=True, verbose_name='Teléfono')

    class Meta:
        verbose_name = 'Conductor'
        verbose_name_plural = 'Conductores'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula})"

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    @property
    def disponible(self):
        return self.activo and self.bus_asignado is None

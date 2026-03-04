import uuid
from django.db import models


class TipoBus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    capacidad_pasajeros = models.IntegerField()
    longitud_metros = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} (cap. {self.capacidad_pasajeros})"


class Bus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    placa = models.CharField(max_length=10, unique=True)
    numero_interno = models.CharField(max_length=10, unique=True)
    tipo = models.ForeignKey(TipoBus, on_delete=models.PROTECT, related_name='buses')
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio_fabricacion = models.IntegerField()
    kilometraje = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"Bus {self.numero_interno} - {self.placa}"


class Conductor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cedula = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    licencia = models.CharField(max_length=20, unique=True)
    turno = models.CharField(max_length=10)
    bus_asignado = models.OneToOneField(Bus, on_delete=models.SET_NULL, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cedula}"
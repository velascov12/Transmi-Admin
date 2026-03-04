import uuid
from django.db import models


class Portal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=100)
    capacidad_buses = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Portal {self.nombre}"


class Ruta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20)
    portal_origen = models.ForeignKey(Portal, on_delete=models.PROTECT, related_name='rutas_origen')
    portal_destino = models.ForeignKey(Portal, on_delete=models.PROTECT, related_name='rutas_destino')
    distancia_km = models.DecimalField(max_digits=6, decimal_places=2)
    tiempo_estimado_min = models.IntegerField()
    frecuencia_min = models.IntegerField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"Ruta {self.codigo} - {self.nombre}"


class HorarioRuta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='horarios')
    dias = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.ruta.codigo} - {self.dias}: {self.hora_inicio}-{self.hora_fin}"
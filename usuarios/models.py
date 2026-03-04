import uuid
from django.db import models


class TipoTarjeta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    descuento_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class UsuarioTullave(models.Model):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('bloqueada', 'Bloqueada'),
        ('vencida', 'Vencida'),
        ('cancelada', 'Cancelada'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_tarjeta = models.CharField(max_length=20, unique=True)
    tipo_tarjeta = models.ForeignKey(TipoTarjeta, on_delete=models.PROTECT, related_name='usuarios')
    nombre_titular = models.CharField(max_length=100)
    cedula_titular = models.CharField(max_length=15, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='activa')
    fecha_expedicion = models.DateField()
    fecha_vencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.numero_tarjeta} - {self.nombre_titular}"


class RecargaTarjeta(models.Model):
    MEDIO_PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('debito', 'Tarjeta Débito'),
        ('credito', 'Tarjeta Crédito'),
        ('pse', 'PSE'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tarjeta = models.ForeignKey(UsuarioTullave, on_delete=models.CASCADE, related_name='recargas')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    medio_pago = models.CharField(max_length=15, choices=MEDIO_PAGO_CHOICES)
    fecha_recarga = models.DateTimeField(auto_now_add=True)
    saldo_anterior = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_posterior = models.DecimalField(max_digits=10, decimal_places=2)
    referencia = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Recarga ${self.monto} - {self.tarjeta.numero_tarjeta}"
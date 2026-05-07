import uuid
from django.db import models

ESTADOS_TARJETA = [
    ('activa', 'Activa'),
    ('bloqueada', 'Bloqueada'),
    ('vencida', 'Vencida'),
    ('perdida', 'Perdida/Robada'),
]

MEDIOS_PAGO = [
    ('efectivo', 'Efectivo'),
    ('debito', 'Tarjeta Débito'),
    ('credito', 'Tarjeta Crédito'),
    ('app', 'App Móvil'),
    ('pse', 'PSE'),
]


class TipoTarjeta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descuento_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='Descuento (%)')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Tipo de Tarjeta'
        verbose_name_plural = 'Tipos de Tarjeta'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    @property
    def total_usuarios(self):
        return self.usuarios.count()


class UsuarioTullave(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_tarjeta = models.CharField(max_length=20, unique=True, verbose_name='N° Tarjeta')
    tipo_tarjeta = models.ForeignKey(TipoTarjeta, on_delete=models.PROTECT, related_name='usuarios', verbose_name='Tipo de Tarjeta')
    nombre_titular = models.CharField(max_length=100, verbose_name='Nombre Titular')
    cedula_titular = models.CharField(max_length=15, unique=True, verbose_name='Cédula Titular')
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Saldo')
    estado = models.CharField(max_length=15, choices=ESTADOS_TARJETA, default='activa', verbose_name='Estado')
    fecha_expedicion = models.DateField(verbose_name='Fecha de Expedición')
    fecha_vencimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de Vencimiento')

    class Meta:
        verbose_name = 'Usuario Tullave'
        verbose_name_plural = 'Usuarios Tullave'
        ordering = ['nombre_titular']

    def __str__(self):
        return f"{self.numero_tarjeta} — {self.nombre_titular}"

    @property
    def esta_activa(self):
        return self.estado == 'activa'

    @property
    def total_recargas(self):
        return self.recargas.count()


class RecargaTarjeta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tarjeta = models.ForeignKey(UsuarioTullave, on_delete=models.CASCADE, related_name='recargas', verbose_name='Tarjeta')
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto')
    medio_pago = models.CharField(max_length=15, choices=MEDIOS_PAGO, verbose_name='Medio de Pago')
    fecha_recarga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    saldo_anterior = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Saldo Anterior')
    saldo_posterior = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Saldo Posterior')
    referencia = models.CharField(max_length=50, unique=True, verbose_name='Referencia')

    class Meta:
        verbose_name = 'Recarga'
        verbose_name_plural = 'Recargas'
        ordering = ['-fecha_recarga']

    def __str__(self):
        return f"Recarga ${self.monto:,.0f} — {self.tarjeta.numero_tarjeta}"

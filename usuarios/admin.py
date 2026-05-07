from django.contrib import admin
from .models import TipoTarjeta, UsuarioTullave, RecargaTarjeta


class RecargaInline(admin.TabularInline):
    model = RecargaTarjeta
    extra = 0
    readonly_fields = ['fecha_recarga', 'referencia', 'saldo_anterior', 'saldo_posterior']
    can_delete = False


@admin.register(TipoTarjeta)
class TipoTarjetaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descuento_porcentaje']
    search_fields = ['nombre']


@admin.register(UsuarioTullave)
class UsuarioTullaveAdmin(admin.ModelAdmin):
    list_display = ['numero_tarjeta', 'nombre_titular', 'cedula_titular', 'tipo_tarjeta', 'saldo', 'estado']
    list_filter = ['estado', 'tipo_tarjeta']
    search_fields = ['numero_tarjeta', 'nombre_titular', 'cedula_titular']
    list_editable = ['estado']
    inlines = [RecargaInline]


@admin.register(RecargaTarjeta)
class RecargaAdmin(admin.ModelAdmin):
    list_display = ['referencia', 'tarjeta', 'monto', 'medio_pago', 'fecha_recarga']
    list_filter = ['medio_pago']
    readonly_fields = ['fecha_recarga']

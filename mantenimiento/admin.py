from django.contrib import admin
from .models import TipoMantenimiento, OrdenMantenimiento, Repuesto, DetalleMantenimiento


class DetalleInline(admin.TabularInline):
    model = DetalleMantenimiento
    extra = 0


@admin.register(TipoMantenimiento)
class TipoMantenimientoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'duracion_estimada_horas', 'periodicidad_km']
    list_filter = ['categoria']
    search_fields = ['nombre']


@admin.register(OrdenMantenimiento)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['numero_orden', 'placa_bus', 'tipo_mantenimiento', 'tecnico_responsable', 'estado', 'fecha_programada']
    list_filter = ['estado', 'tipo_mantenimiento']
    search_fields = ['numero_orden', 'placa_bus', 'tecnico_responsable']
    date_hierarchy = 'fecha_programada'
    inlines = [DetalleInline]


@admin.register(Repuesto)
class RepuestoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'stock_actual', 'stock_minimo', 'precio_unitario']
    search_fields = ['codigo', 'nombre']
    list_editable = ['stock_actual']

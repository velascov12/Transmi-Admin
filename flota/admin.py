from django.contrib import admin
from .models import TipoBus, Bus, Conductor


@admin.register(TipoBus)
class TipoBusAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'capacidad_pasajeros', 'longitud_metros', 'total_buses']
    search_fields = ['nombre']

    def total_buses(self, obj):
        return obj.total_buses
    total_buses.short_description = 'Buses'


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ['numero_interno', 'placa', 'tipo', 'marca', 'modelo', 'estado', 'fecha_ingreso']
    list_filter = ['estado', 'tipo', 'marca']
    search_fields = ['placa', 'numero_interno', 'marca']
    list_editable = ['estado']
    date_hierarchy = 'fecha_ingreso'


@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'cedula', 'licencia', 'turno', 'bus_asignado', 'activo']
    list_filter = ['activo', 'turno']
    search_fields = ['nombre', 'apellido', 'cedula']
    list_editable = ['activo']

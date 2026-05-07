from django.contrib import admin
from .models import Portal, Ruta, HorarioRuta


class HorarioRutaInline(admin.TabularInline):
    model = HorarioRuta
    extra = 1


@admin.register(Portal)
class PortalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'localidad', 'capacidad_buses', 'activo']
    list_filter = ['activo', 'localidad']
    search_fields = ['nombre', 'localidad']
    list_editable = ['activo']


@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'tipo', 'portal_origen', 'portal_destino', 'activa']
    list_filter = ['tipo', 'activa']
    search_fields = ['codigo', 'nombre']
    inlines = [HorarioRutaInline]
    list_editable = ['activa']


@admin.register(HorarioRuta)
class HorarioRutaAdmin(admin.ModelAdmin):
    list_display = ['ruta', 'dias', 'hora_inicio', 'hora_fin']
    list_filter = ['dias']

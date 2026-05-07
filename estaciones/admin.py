from django.contrib import admin
from .models import Estacion, TaquillaCarga, IncidenciaEstacion


class TaquillaInline(admin.TabularInline):
    model = TaquillaCarga
    extra = 0


class IncidenciaInline(admin.TabularInline):
    model = IncidenciaEstacion
    extra = 0
    fields = ['tipo', 'descripcion', 'estado']


@admin.register(Estacion)
class EstacionAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'tipo', 'localidad', 'en_operacion']
    list_filter = ['tipo', 'localidad', 'en_operacion', 'tiene_biciparqueo']
    search_fields = ['codigo', 'nombre', 'localidad']
    list_editable = ['en_operacion']
    inlines = [TaquillaInline, IncidenciaInline]


@admin.register(TaquillaCarga)
class TaquillaAdmin(admin.ModelAdmin):
    list_display = ['estacion', 'numero', 'operativa', 'ultima_revision']
    list_filter = ['operativa']


@admin.register(IncidenciaEstacion)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ['estacion', 'tipo', 'estado', 'fecha_reporte']
    list_filter = ['tipo', 'estado']
    search_fields = ['estacion__nombre', 'descripcion']

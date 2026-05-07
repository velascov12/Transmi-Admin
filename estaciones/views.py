from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Estacion, IncidenciaEstacion
from .forms import EstacionForm, IncidenciaForm


def lista_estaciones(request):
    estaciones = Estacion.objects.all()
    q = request.GET.get('q', '')
    if q:
        estaciones = estaciones.filter(Q(codigo__icontains=q) | Q(nombre__icontains=q))
    return render(request, 'estaciones/estacion_lista.html', {'estaciones': estaciones, 'q': q})


def crear_estacion(request):
    if request.method == 'POST':
        form = EstacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estacion creada.')
            return redirect('estaciones:lista_estaciones')
    else:
        form = EstacionForm()
    return render(request, 'estaciones/estacion_form.html', {'form': form, 'accion': 'Crear'})


def editar_estacion(request, pk):
    estacion = get_object_or_404(Estacion, pk=pk)
    if request.method == 'POST':
        form = EstacionForm(request.POST, instance=estacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estacion actualizada.')
            return redirect('estaciones:lista_estaciones')
    else:
        form = EstacionForm(instance=estacion)
    return render(request, 'estaciones/estacion_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_estacion(request, pk):
    estacion = get_object_or_404(Estacion, pk=pk)
    if request.method == 'POST':
        estacion.delete()
        messages.success(request, 'Estacion eliminada.')
        return redirect('estaciones:lista_estaciones')
    return render(request, 'estaciones/confirmar_eliminar.html', {'objeto': estacion})


# -- incidencias --

def lista_incidencias(request):
    incidencias = IncidenciaEstacion.objects.select_related('estacion').all()
    return render(request, 'estaciones/incidencia_lista.html', {'incidencias': incidencias})


def crear_incidencia(request):
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Incidencia registrada.')
            return redirect('estaciones:lista_incidencias')
    else:
        form = IncidenciaForm()
    return render(request, 'estaciones/incidencia_form.html', {'form': form, 'accion': 'Crear'})


def editar_incidencia(request, pk):
    incidencia = get_object_or_404(IncidenciaEstacion, pk=pk)
    if request.method == 'POST':
        form = IncidenciaForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Incidencia actualizada.')
            return redirect('estaciones:lista_incidencias')
    else:
        form = IncidenciaForm(instance=incidencia)
    return render(request, 'estaciones/incidencia_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_incidencia(request, pk):
    incidencia = get_object_or_404(IncidenciaEstacion, pk=pk)
    if request.method == 'POST':
        incidencia.delete()
        messages.success(request, 'Incidencia eliminada.')
        return redirect('estaciones:lista_incidencias')
    return render(request, 'estaciones/confirmar_eliminar.html', {'objeto': incidencia})

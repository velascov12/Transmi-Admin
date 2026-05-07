from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q, F

from .models import OrdenMantenimiento, Repuesto
from .forms import OrdenMantenimientoForm, RepuestoForm


def lista_ordenes(request):
    ordenes = OrdenMantenimiento.objects.select_related('tipo_mantenimiento').all()
    q = request.GET.get('q', '')
    if q:
        ordenes = ordenes.filter(Q(numero_orden__icontains=q) | Q(placa_bus__icontains=q))
    return render(request, 'mantenimiento/orden_lista.html', {'ordenes': ordenes, 'q': q})


def crear_orden(request):
    if request.method == 'POST':
        form = OrdenMantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden creada.')
            return redirect('mantenimiento:lista_ordenes')
    else:
        form = OrdenMantenimientoForm()
    return render(request, 'mantenimiento/orden_form.html', {'form': form, 'accion': 'Crear'})


def editar_orden(request, pk):
    orden = get_object_or_404(OrdenMantenimiento, pk=pk)
    if request.method == 'POST':
        form = OrdenMantenimientoForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden actualizada.')
            return redirect('mantenimiento:lista_ordenes')
    else:
        form = OrdenMantenimientoForm(instance=orden)
    return render(request, 'mantenimiento/orden_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_orden(request, pk):
    orden = get_object_or_404(OrdenMantenimiento, pk=pk)
    if request.method == 'POST':
        orden.delete()
        messages.success(request, 'Orden eliminada.')
        return redirect('mantenimiento:lista_ordenes')
    return render(request, 'mantenimiento/confirmar_eliminar.html', {'objeto': orden})


# -- repuestos --

def lista_repuestos(request):
    repuestos = Repuesto.objects.all()
    q = request.GET.get('q', '')
    if q:
        repuestos = repuestos.filter(Q(codigo__icontains=q) | Q(nombre__icontains=q))
    return render(request, 'mantenimiento/repuesto_lista.html', {'repuestos': repuestos, 'q': q})


def crear_repuesto(request):
    if request.method == 'POST':
        form = RepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Repuesto creado.')
            return redirect('mantenimiento:lista_repuestos')
    else:
        form = RepuestoForm()
    return render(request, 'mantenimiento/repuesto_form.html', {'form': form, 'accion': 'Crear'})


def editar_repuesto(request, pk):
    repuesto = get_object_or_404(Repuesto, pk=pk)
    if request.method == 'POST':
        form = RepuestoForm(request.POST, instance=repuesto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Repuesto actualizado.')
            return redirect('mantenimiento:lista_repuestos')
    else:
        form = RepuestoForm(instance=repuesto)
    return render(request, 'mantenimiento/repuesto_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_repuesto(request, pk):
    repuesto = get_object_or_404(Repuesto, pk=pk)
    if request.method == 'POST':
        try:
            repuesto.delete()
            messages.success(request, 'Repuesto eliminado.')
        except Exception:
            messages.error(request, 'No se puede eliminar, esta en uso.')
        return redirect('mantenimiento:lista_repuestos')
    return render(request, 'mantenimiento/confirmar_eliminar.html', {'objeto': repuesto})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Bus, Conductor, TipoBus
from .forms import BusForm, ConductorForm


def lista_buses(request):
    buses = Bus.objects.select_related('tipo').all()
    q = request.GET.get('q', '')
    if q:
        buses = buses.filter(Q(placa__icontains=q) | Q(numero_interno__icontains=q))
    return render(request, 'flota/bus_lista.html', {'buses': buses, 'q': q})


def crear_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bus registrado.')
            return redirect('flota:lista_buses')
    else:
        form = BusForm()
    return render(request, 'flota/bus_form.html', {'form': form, 'accion': 'Crear'})


def editar_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bus actualizado.')
            return redirect('flota:lista_buses')
    else:
        form = BusForm(instance=bus)
    return render(request, 'flota/bus_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == 'POST':
        bus.delete()
        messages.success(request, 'Bus eliminado.')
        return redirect('flota:lista_buses')
    return render(request, 'flota/confirmar_eliminar.html', {'objeto': bus})


# -- conductores --

def lista_conductores(request):
    conductores = Conductor.objects.select_related('bus_asignado').all()
    q = request.GET.get('q', '')
    if q:
        conductores = conductores.filter(Q(nombre__icontains=q) | Q(apellido__icontains=q))
    return render(request, 'flota/conductor_lista.html', {'conductores': conductores, 'q': q})


def crear_conductor(request):
    if request.method == 'POST':
        form = ConductorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor registrado.')
            return redirect('flota:lista_conductores')
    else:
        form = ConductorForm()
    return render(request, 'flota/conductor_form.html', {'form': form, 'accion': 'Crear'})


def editar_conductor(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    if request.method == 'POST':
        form = ConductorForm(request.POST, instance=conductor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor actualizado.')
            return redirect('flota:lista_conductores')
    else:
        form = ConductorForm(instance=conductor)
    return render(request, 'flota/conductor_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_conductor(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    if request.method == 'POST':
        conductor.delete()
        messages.success(request, 'Conductor eliminado.')
        return redirect('flota:lista_conductores')
    return render(request, 'flota/confirmar_eliminar.html', {'objeto': conductor})

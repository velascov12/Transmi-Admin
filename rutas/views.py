from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Ruta, Portal
from .forms import RutaForm, PortalForm


def lista_rutas(request):
    rutas = Ruta.objects.select_related('portal_origen', 'portal_destino').all()
    q = request.GET.get('q', '')
    if q:
        rutas = rutas.filter(Q(codigo__icontains=q) | Q(nombre__icontains=q))
    return render(request, 'rutas/ruta_lista.html', {'rutas': rutas, 'q': q})


def crear_ruta(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta creada.')
            return redirect('rutas:lista_rutas')
    else:
        form = RutaForm()
    return render(request, 'rutas/ruta_form.html', {'form': form, 'accion': 'Crear'})


def editar_ruta(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    if request.method == 'POST':
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta actualizada.')
            return redirect('rutas:lista_rutas')
    else:
        form = RutaForm(instance=ruta)
    return render(request, 'rutas/ruta_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_ruta(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    if request.method == 'POST':
        ruta.delete()
        messages.success(request, 'Ruta eliminada.')
        return redirect('rutas:lista_rutas')
    return render(request, 'rutas/confirmar_eliminar.html', {'objeto': ruta})


# -- portales --

def lista_portales(request):
    portales = Portal.objects.all()
    return render(request, 'rutas/portal_lista.html', {'portales': portales})


def crear_portal(request):
    if request.method == 'POST':
        form = PortalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Portal creado.')
            return redirect('rutas:lista_portales')
    else:
        form = PortalForm()
    return render(request, 'rutas/portal_form.html', {'form': form, 'accion': 'Crear'})


def editar_portal(request, pk):
    portal = get_object_or_404(Portal, pk=pk)
    if request.method == 'POST':
        form = PortalForm(request.POST, instance=portal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Portal actualizado.')
            return redirect('rutas:lista_portales')
    else:
        form = PortalForm(instance=portal)
    return render(request, 'rutas/portal_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_portal(request, pk):
    portal = get_object_or_404(Portal, pk=pk)
    if request.method == 'POST':
        try:
            portal.delete()
            messages.success(request, 'Portal eliminado.')
        except Exception:
            messages.error(request, 'No se puede eliminar, tiene rutas asociadas.')
        return redirect('rutas:lista_portales')
    return render(request, 'rutas/confirmar_eliminar.html', {'objeto': portal})

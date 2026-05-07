from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
import uuid

from .models import UsuarioTullave, TipoTarjeta, RecargaTarjeta
from .forms import UsuarioTullaveForm, RecargaForm


def lista_usuarios(request):
    usuarios = UsuarioTullave.objects.select_related('tipo_tarjeta').all()
    q = request.GET.get('q', '')
    if q:
        usuarios = usuarios.filter(Q(nombre_titular__icontains=q) | Q(numero_tarjeta__icontains=q))
    return render(request, 'usuarios/usuario_lista.html', {'usuarios': usuarios, 'q': q})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioTullaveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado.')
            return redirect('usuarios:lista_usuarios')
    else:
        form = UsuarioTullaveForm()
    return render(request, 'usuarios/usuario_form.html', {'form': form, 'accion': 'Crear'})


def editar_usuario(request, pk):
    usuario = get_object_or_404(UsuarioTullave, pk=pk)
    if request.method == 'POST':
        form = UsuarioTullaveForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado.')
            return redirect('usuarios:lista_usuarios')
    else:
        form = UsuarioTullaveForm(instance=usuario)
    return render(request, 'usuarios/usuario_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_usuario(request, pk):
    usuario = get_object_or_404(UsuarioTullave, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado.')
        return redirect('usuarios:lista_usuarios')
    return render(request, 'usuarios/confirmar_eliminar.html', {'objeto': usuario})


def recargar_tarjeta(request, pk):
    usuario = get_object_or_404(UsuarioTullave, pk=pk)
    if request.method == 'POST':
        form = RecargaForm(request.POST)
        if form.is_valid():
            monto = form.cleaned_data['monto']
            saldo_anterior = usuario.saldo
            usuario.saldo += monto
            usuario.save()
            RecargaTarjeta.objects.create(
                tarjeta=usuario,
                monto=monto,
                medio_pago=form.cleaned_data['medio_pago'],
                saldo_anterior=saldo_anterior,
                saldo_posterior=usuario.saldo,
                referencia=f"REF-{uuid.uuid4().hex[:8].upper()}",
            )
            messages.success(request, f'Recarga de ${monto:,.0f} realizada.')
            return redirect('usuarios:lista_usuarios')
    else:
        form = RecargaForm()
    return render(request, 'usuarios/recarga_form.html', {'form': form, 'usuario': usuario})

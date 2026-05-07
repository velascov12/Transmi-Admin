from django import forms
from .models import Ruta, Portal


class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['codigo', 'nombre', 'tipo', 'portal_origen', 'portal_destino',
                  'distancia_km', 'tiempo_estimado_min', 'frecuencia_min', 'activa']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'portal_origen': forms.Select(attrs={'class': 'form-select'}),
            'portal_destino': forms.Select(attrs={'class': 'form-select'}),
            'distancia_km': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'tiempo_estimado_min': forms.NumberInput(attrs={'class': 'form-control'}),
            'frecuencia_min': forms.NumberInput(attrs={'class': 'form-control'}),
            'activa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        origen = cleaned_data.get('portal_origen')
        destino = cleaned_data.get('portal_destino')
        if origen and destino and origen == destino:
            raise forms.ValidationError('el portal origen y destino no pueden ser el mismo')
        return cleaned_data

    def clean_codigo(self):
        return self.cleaned_data.get('codigo', '').strip().upper()


class PortalForm(forms.ModelForm):
    class Meta:
        model = Portal
        fields = ['nombre', 'ubicacion', 'localidad', 'capacidad_buses', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_buses': forms.NumberInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

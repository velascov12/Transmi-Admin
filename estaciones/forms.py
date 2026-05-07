from django import forms
from .models import Estacion, IncidenciaEstacion


class EstacionForm(forms.ModelForm):
    class Meta:
        model = Estacion
        fields = ['codigo', 'nombre', 'tipo', 'localidad', 'direccion',
                  'tiene_biciparqueo', 'tiene_ascensor', 'en_operacion']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'tiene_biciparqueo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tiene_ascensor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'en_operacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_codigo(self):
        return self.cleaned_data.get('codigo', '').strip().upper()


class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = IncidenciaEstacion
        fields = ['estacion', 'tipo', 'descripcion', 'estado']
        widgets = {
            'estacion': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

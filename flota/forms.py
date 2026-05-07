from django import forms
from .models import Bus, Conductor


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['placa', 'numero_interno', 'tipo', 'marca', 'modelo',
                  'anio_fabricacion', 'kilometraje', 'estado', 'fecha_ingreso']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_interno': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio_fabricacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_placa(self):
        return self.cleaned_data.get('placa', '').strip().upper()


class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ['cedula', 'nombre', 'apellido', 'licencia', 'turno',
                  'bus_asignado', 'activo', 'fecha_contratacion', 'telefono']
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'licencia': forms.TextInput(attrs={'class': 'form-control'}),
            'turno': forms.Select(attrs={'class': 'form-select'}),
            'bus_asignado': forms.Select(attrs={'class': 'form-select'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_contratacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula', '').strip()
        if not cedula.isdigit():
            raise forms.ValidationError('la cedula solo debe contener numeros')
        return cedula

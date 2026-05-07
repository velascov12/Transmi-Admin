from django import forms
from .models import OrdenMantenimiento, Repuesto


class OrdenMantenimientoForm(forms.ModelForm):
    class Meta:
        model = OrdenMantenimiento
        fields = ['numero_orden', 'placa_bus', 'tipo_mantenimiento', 'tecnico_responsable',
                  'fecha_programada', 'kilometraje_bus', 'estado', 'observaciones']
        widgets = {
            'numero_orden': forms.TextInput(attrs={'class': 'form-control'}),
            'placa_bus': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_mantenimiento': forms.Select(attrs={'class': 'form-select'}),
            'tecnico_responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_programada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'kilometraje_bus': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_numero_orden(self):
        return self.cleaned_data.get('numero_orden', '').strip().upper()

    def clean_placa_bus(self):
        return self.cleaned_data.get('placa_bus', '').strip().upper()


class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['codigo', 'nombre', 'descripcion', 'stock_actual', 'stock_minimo', 'precio_unitario']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'stock_actual': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'stock_minimo': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def clean_stock_actual(self):
        s = self.cleaned_data.get('stock_actual')
        if s is not None and s < 0:
            raise forms.ValidationError('el stock no puede ser negativo')
        return s

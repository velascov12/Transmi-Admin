from django import forms
from .models import UsuarioTullave, MEDIOS_PAGO


class UsuarioTullaveForm(forms.ModelForm):
    class Meta:
        model = UsuarioTullave
        fields = ['numero_tarjeta', 'tipo_tarjeta', 'nombre_titular', 'cedula_titular',
                  'saldo', 'estado', 'fecha_expedicion']
        widgets = {
            'numero_tarjeta': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_tarjeta': forms.Select(attrs={'class': 'form-select'}),
            'nombre_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_cedula_titular(self):
        cedula = self.cleaned_data.get('cedula_titular', '').strip()
        if not cedula.isdigit():
            raise forms.ValidationError('la cedula solo debe contener numeros')
        return cedula


class RecargaForm(forms.Form):
    monto = forms.DecimalField(
        max_digits=10, decimal_places=2, min_value=1000,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1000', 'step': '500'})
    )
    medio_pago = forms.ChoiceField(
        choices=MEDIOS_PAGO,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def clean_monto(self):
        monto = self.cleaned_data.get('monto')
        if monto and monto < 1000:
            raise forms.ValidationError('el monto minimo es $1,000')
        return monto

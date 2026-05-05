from django import forms
from .models import Vino

class VinoForm(forms.ModelForm):
    class Meta:
        model = Vino
        fields = ['nombre', 'precio', 'tipo', 'bodega']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'bodega': forms.Select(attrs={'class': 'form-control'}),
        }

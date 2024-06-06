from django import forms
from .models import DestinoTuristico

class DestinoTuristicoForm(forms.ModelForm):
    class Meta:
        model = DestinoTuristico
        fields = ['nombre', 'descripcion', 'imagen', 'precio', 'oferta']

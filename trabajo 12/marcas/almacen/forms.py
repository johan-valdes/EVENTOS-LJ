from django import forms 
from.models import Prenda

class PrendaForm(forms.ModelForm): 
    class Meta: 
        model = Prenda
        fields = ['tipo', 'marca', 'talla', 'color']
        
    def clean(self):
        cleaned_data = super().clean()
        for field in ['tipo', 'marca', 'talla', 'color']:
            if not cleaned_data.get(field):
                self.add_error(field, 'Este campo es obligatorio.')
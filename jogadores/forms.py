from django import forms
from .models import Personagem, Classe, Raca

class PersonagemForm(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = ['nome', 'classe', 'raca', 'nivel']
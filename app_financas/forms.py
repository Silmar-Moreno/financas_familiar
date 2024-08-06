from django import forms
from .models import Transacao, Categoria

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'tipo', 'descricao', 'valor', 'categoria']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
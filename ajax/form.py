from django import forms

from ajax.models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria']

        widgets = {
            'categoria': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Período',
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
            })
        }

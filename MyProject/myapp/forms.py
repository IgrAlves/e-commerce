from django import forms
from django.forms import ModelForm
from myapp.models import *

class ProductForm(forms.ModelForm):
    class Meta:

        model = Product
        fields = "__all__"
        labels = {
            "name": "nome",
            "descript": "descrição",
            "price": "preço",
            "path": "imagem",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do item",
                }
            ),
            'descript': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Escreva uma breve descrição",
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "150.00",
                }
            ),
            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Imagem",
                }
            ),
        }
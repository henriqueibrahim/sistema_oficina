from django import forms
from .models import Clientes

class Form_Clientes(forms.ModelForm):
    nome = forms.CharField(max_length=256)
    sobrenome = forms.CharField(max_length=256)
    endereco = forms.CharField(max_length=256)
    telefone = forms.CharField(max_length=35)
    email = forms.EmailField(max_length=256)

    class Meta:
        model = Clientes
        fields = "__all__"
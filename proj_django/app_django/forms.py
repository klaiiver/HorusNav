from django import forms
from . models import Usuarios, Posicao


class Form_usuarios(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome','dest']

class Form_desc(forms.ModelForm):
    class Meta:
        model = Posicao
        fields = ['descricao']

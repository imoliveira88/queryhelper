from django.forms import ModelForm
from django import forms
from aplicacao.models import Sistema, Query, Modulo


class SistemaForm(ModelForm):
    class Meta:
        model = Sistema
        fields = '__all__'
        #exclude = ['host', 'participants']

class QueryForm(ModelForm):
    query = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", "cols":"600",'class':'form-control','placeholder': 'Query'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows":"2", "cols":"100",'class':'form-control','placeholder': 'Descrição'}))
    class Meta:
        model = Query
        fields = '__all__'

class ModuloForm(ModelForm):
    class Meta:
        model = Modulo
        fields = '__all__'

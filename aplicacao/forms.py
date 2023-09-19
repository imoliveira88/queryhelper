from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from aplicacao.models import Sistema, Query


class SistemaForm(ModelForm):
    class Meta:
        model = Sistema
        fields = '__all__'
        #exclude = ['host', 'participants']

class QueryForm(ModelForm):
    query = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", "cols":"600"}))
    class Meta:
        model = Query
        fields = '__all__'
        #exclude = ['host', 'participants']

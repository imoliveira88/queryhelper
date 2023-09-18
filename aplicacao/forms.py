from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from aplicacao.models import Sistema, Query


class SistemaForm(ModelForm):
    class Meta:
        model = Sistema
        fields = '__all__'
        #exclude = ['host', 'participants']

class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = '__all__'
        #exclude = ['host', 'participants']

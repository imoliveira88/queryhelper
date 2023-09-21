import django_filters
from django_filters import CharFilter, ModelChoiceFilter
from aplicacao.models import Modulo, Query, Sistema
from django import forms

class QueryFilter(django_filters.FilterSet):
    filtro_descricao = CharFilter(field_name="descricao",label="Descrição contém", lookup_expr="icontains") #Outras opções "iexact"
    filtro_sistema = ModelChoiceFilter(field_name="sistema",queryset=Sistema.objects.all(),label="Sistema",widget=forms.Select(attrs={'class':'form-control'}))
    filtro_modulo = ModelChoiceFilter(field_name="modulo",queryset=Modulo.objects.all(),label="Modulo",widget=forms.Select(attrs={'class':'form-control'}))

    #query = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", "cols":"600"}))
    #descricao = forms.CharField(widget=forms.Textarea(attrs={"rows":"2", "cols":"100"}))

    class Meta:
        model = Query
        fields = ['filtro_descricao','filtro_sistema','filtro_modulo']

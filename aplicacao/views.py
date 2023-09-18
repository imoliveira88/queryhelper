from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from aplicacao.forms import QueryForm, SistemaForm

from aplicacao.models import Query, Sistema

# Create your views here.
def app_view(request):
    return render(request, 'pages/sistemas.html', context={'name':'Igor'})

def lista_queries(request):
    query = Query.objects.all
    context = {'queries': query}
    return render(request, "pages/queries.html", context)

def inclui_query(request):
    context = {}
    form = QueryForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'pages/inclui_query.html', context)

def deleta_query(request, id):
    context ={}

    obj = get_object_or_404(Query, id=id)
    obj.delete()

    return render(request, "pages/queries.html", context)

def inclui_sistema(request):
    context = {}
    form = SistemaForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'pages/inclui_sistema.html', context)

def deleta_sistema(request, id):
    context ={}

    obj = get_object_or_404(Sistema, id=id)
    obj.delete()

    return render(request, "pages/sistemas.html", context)

def lista_sistemas(request):
    sistemas = Sistema.objects.all

    context = {'sistemas': sistemas}
    return render(request, "pages/sistemas.html", context)

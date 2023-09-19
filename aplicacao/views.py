from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from aplicacao.forms import QueryForm, SistemaForm
from django.urls import reverse
from django.contrib import messages

from aplicacao.models import Query, Sistema

# Create your views here.
def app_view(request):
    return render(request, 'pages/sistemas.html')

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
    if request.POST:
        return HttpResponseRedirect('lista_queries')
    else:
        return render(request, 'pages/inclui_query.html',context)

def deleta_query(request, id):

    try:
        obj = get_object_or_404(Query, id=id)
        obj.delete()
        messages.info(request, "Query excluída com sucesso!")
    except Exception:
        messages.error(request, "Erro na tentativa de exclusão da query!")

    return HttpResponseRedirect('/aplicacao/lista_queries')

def inclui_sistema(request):
    context = {}
    form = SistemaForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    if request.POST:
        return HttpResponseRedirect('lista_sistemas')
    else:
        return render(request, 'pages/inclui_sistema.html',context)


def deleta_sistema(request, id):

    try:
        obj = get_object_or_404(Sistema, id=id)
        obj.delete()
        messages.info(request, "Sistema excluído com sucesso!")
    except Exception:
        messages.error(request, "Não foi possível excluir o sistema por haver queries cadastradas nele!")

    return HttpResponseRedirect('/')

def lista_sistemas(request):
    sistemas = Sistema.objects.all

    context = {'sistemas': sistemas}
    return render(request, "pages/sistemas.html", context)

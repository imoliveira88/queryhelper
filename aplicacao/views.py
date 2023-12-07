from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from aplicacao.forms import QueryForm, SistemaForm, ModuloForm
from django.urls import reverse
from django.contrib import messages
from aplicacao.filters import QueryFilter
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from aplicacao.models import Query, Sistema, Modulo

# Create your views here.
def app_view(request):
    return render(request, 'pages/sistemas.html')

def lista_queries(request):
    query_list = Query.objects.all()

    paginator = Paginator(query_list, 10)  # Show 10 queries per page
    page = request.GET.get('page')  # Fix the parameter name

    try:
        queries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        queries = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results.
        queries = paginator.page(paginator.num_pages)

    return render(request, 'pages/queries.html', {'queries': queries})

    #context = {'queries': query}
    #return render(request, "pages/queries.html", context)

def edita_query(request, id):
    query = Query.objects.get(id=id)
    if request.method == 'GET':
        context = {'form' : QueryForm(instance=query), 'id':id}
        return render(request,'pages/edita_query.html',context)
#usar strip
    elif request.method == 'POST':
        form = QueryForm(request.POST or None)
        context = {'form': form}
        query.nome = form["nome"].data
        query.query = form["query"].data
        query.descricao = form["descricao"].data
        query.save()
        query = Query.objects.all
        context = {'queries': query}
        return render(request, 'pages/queries.html',context)

def lista_modulos(request):
    modulos = Modulo.objects.all
    context = {'modulos': modulos}
    return render(request, "pages/modulos.html", context)

def deleta_modulo(request, id):

    try:
        obj = get_object_or_404(Modulo, id=id)
        obj.delete()
        messages.info(request, "Módulo excluído com sucesso!")
    except Exception:
        messages.error(request, "Erro na tentativa de exclusão do módulo!")

    return HttpResponseRedirect('/aplicacao/lista_modulos')

def inclui_modulo(request):
    context = {}
    form = ModuloForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    if request.POST:
        return HttpResponseRedirect('lista_modulos')
    else:
        return render(request, 'pages/inclui_modulo.html',context)

def queries_por_sistema(request):
    filtro = QueryFilter(request.GET, queryset=Query.objects.all())

    context = {'filtro': filtro}
    return render(request, "pages/relatorios.html", context)

def sobre(request):
    return render(request, "pages/sobre.html")

def exibe_query(request, id):
    query = Query.objects.get(id=id)
    context = {'query': query}
    return render(request, "pages/exibe_query.html", context)

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

def query_oracle_database(request):
    # Connect to the Oracle database
    connection = cx_Oracle.connect(
        user="SINC_INADIPLENTES",
        password="AN4LISYS_IN4D1",
        dsn="192.168.1.46:1521/piramide.intranet.copergas.com.br"
    )

    # Create a cursor
    cursor = connection.cursor()

    # Execute a sample query (replace with your actual query)
    query = "SELECT 1, 2 FROM ITENS_PED_COMPRA FETCH FIRST 10 ROWS ONLY"
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Process the data or pass it to a template
    data = [{'column1': row[0], 'column2': row[1]} for row in rows]

    return render(request, 'pages/teste.html', {'data': data})
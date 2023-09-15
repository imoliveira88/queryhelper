from django.shortcuts import render
from django.http import HttpResponse

from aplicacao.models import Query

# Create your views here.
def piramide_view(request):
    return render(request, 'base.html', context={'name':'Igor'})

def todas_queries(request):
    query = Query.objects.all;


def home_view(request):
    return HttpResponse('HOME')


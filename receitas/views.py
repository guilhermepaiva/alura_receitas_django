from django.shortcuts import render
from django.http import HttpResponse
from .models import Receita


def index(request):
    receitas = Receita.objects.all()
    dados = {
        'receitas':receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')

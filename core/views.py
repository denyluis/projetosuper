from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')

def contato(request):
    return render(request,'contato.html')

def produto(request):
    return render(request,'produto.html')

def produtos(request):
    return render(request,'produtos.html')
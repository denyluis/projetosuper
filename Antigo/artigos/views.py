from django.shortcuts import render

# Create your views here.
from .models import Artigo

def artigo_list(request):
    artigos =Artigo.objects.all()

    context = {
        'artigos_list': artigos,
    }

    return render(request,'artigos/artigo_list.html',context)
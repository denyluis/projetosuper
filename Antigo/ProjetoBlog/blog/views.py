from django.shortcuts import render
from .models import Post

from django.http.response import HttpResponse
# Create your views here.

def index(request):
    return render(request,'blog/index.html')
def   post_list(request):
    posts = Post.objects.all()

    context = {
        'post_list': posts
    }
    return render(request,'blog/post_list.html',context)
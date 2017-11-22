from django.contrib import admin

# Register your models here.

from  .models import Autor,Artigo
admin.site.register(Autor)
admin.site.register(Artigo)
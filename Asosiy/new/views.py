from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def about(request ):
    ab = {
        'ozim_haqimda':About.objects.all()
    }
    return render(request, 'about.html', ab)

def about_rasm(request, son):
    rasm = {
    'r':About.objects.get(id=son)
    }
    return render(request, 'about.html', rasm)

def blog(request):

    std = {
        'maqolalar':Maqola.objects.all()
    }
    return render(request, 'blog.html',std)

def maqola_batafsil(request, son):
    std = {
        'm': Maqola.objects.get(id=son)
    }
    return render(request,'maqola.html',std)



def intervyu(request):
    int = {
        'intervyular': Intervyu.objects.all()
    }
    return render(request, 'intervyu.html', int)

def intervyu_batafsil(request, son):
    int = {
        'i': Intervyu.objects.get(id=son)
    }
    return render(request,'intervyu_sarlavha.html',int)

def maqola(request):
    return render(request, 'maqola.html')
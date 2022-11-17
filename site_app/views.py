from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Disco
from .forms import DiscoForm


# Create your views here.

def inicio(request):
    return render(request, 'pages/main_page.html')

def pagina_bandas(request):
    return render(request, 'pages/bands_page.html')

def pagina_acerca(request):
    return render(request, 'pages/about_page.html')

def discos(request):
    discos = Disco.objects.all()
    return render(request, 'discos/index.html', {'discos':discos})

def crear_disco(request):
    formulario = DiscoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('/discs')
    return render(request, 'discos/crear.html',{'formulario':formulario})

def editar_disco(request, id):
    disco = Disco.objects.get(id=id)
    formulario = DiscoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('/discs')
    return render(request, 'discos/editar.html', {'formulario':formulario})

def borrar_disco(request, id):
    disco = Disco.objects.get(id=id)
    disco.delete()
    return redirect('/discs')


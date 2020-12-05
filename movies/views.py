from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,'MovieDick_Inicio.html')

def catalogo(request):
    return render(request,'Catalogo.html')

def categoria(request):
    return render(request,'Categoria.html')

def lista_pelicula(request):
    return render(request,'Lista_Peliculas.html')

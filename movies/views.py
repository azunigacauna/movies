from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from MovieDick.models import Pelicula, Lista

from fusioncharts import FusionCharts
from pprint import pprint
from collections import OrderedDict

def not_found(request):
    return render(request, 'pag_no_encontrada.html')

# Create your views here.
def inicio(request):
    return render(request,'MovieDick_Inicio.html')

def catalogo(request):
    return render(request,'Catalogo.html')

def lista_pelicula(request):
    return render(request,'Lista_Peliculas.html')

def ini_sesion(request):
  if request.method=='POST':
    username = request.POST['usuario']
    password = request.POST['contraseña']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request, user)
      return redirect("/")
    else:
      messages.info(request, 'Credenciales inválidas')
      return redirect('/inicio_sesion')
  else:
    return render(request,'inicio_sesion.html')

def registro(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']
    if password1==password2:
      if User.objects.filter(username=username).exists():
        messages.info(request, 'Usuario ya existente')
        return redirect('register')
      elif User.objects.filter(email=email).exists():
        messages.info(request, 'Email ya existente')
        return redirect('register')
      else:
        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save();
        print('Usuario creado')
        return redirect('login')
    else:
      messages.info(request, 'Las contraseñas no coinciden')
      return redirect('register')
    return redirect('/')
  else:
    return render(request, 'Registro.html')

def logout(request):
  auth.logout(request)
  return redirect('/')

def perfil(request):
    return render(request, 'Perfil.html')

def resenia(request):
    angularGauge = FusionCharts("angulargauge", "ex1" , "450", "270", "chart-1", "json",
        """{
            "chart": {
                "caption": "Ratio de calificacion",
                "lowerLimit": "0",
                "upperLimit": "10",
                "showValue": "55",
                "theme": "fusion",
                "showToolTip": "0"
            },
            "colorRange": {
                "color": [{
                    "minValue": "0",
                    "maxValue": "5",
                    "code": "#F2726F"
                }, {
                    "minValue": "5",
                    "maxValue": "7",
                    "code": "#FFC533"
                }, {
                    "minValue": "7",
                    "maxValue": "10",
                    "code": "#62B58F"
                }]
            },
            "dials": {
                "dial": [{
                    "value": "7"
                }]
            }
        }""")
    return  render(request, 'Resenia_Pelicula.html', {'output' : angularGauge.render()})

def chart2(request):
   chartObj = FusionCharts( 'pie3d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Cantidad de Películas por Género",
    "showvalues": "1",
    "showpercentintooltip": "0",
    "enablemultislicing": "1",
    "theme": "fusion"
  },
  "data": [
    {
      "label": "Terror",
      "value": "14",
      "color": "black",
    },
    {
      "label": "Comedia",
      "value": "23"
    },
    {
      "label": "Accion",
      "value": "18"
    },
    {
      "label": "Drama",
      "value": "27"
    },
    {
      "label": "Sci-Fi",
      "value": "6"
    }
  ]
}""")
   return render(request, 'Categoria.html', {'output': chartObj.render()})


#GRAFICO DE BARRAS en pagina de inicio
def chart3(request):
   chartObj = FusionCharts( 'column2d', 'ex1', '500', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Generos mas vistos",
    "subcaption": "",
    "xaxisname": "Genero",
    "yaxisname": "vistas por mes",
    "theme": "Candy"
  },
  "data": [
    {
      "label": "Accion",
      "value": "290"
    },
    {
      "label": "Animacion",
      "value": "260"
    },
    {
      "label": "Fantasia",
      "value": "180"
    },
    {
      "label": "Musicales",
      "value": "140"
    },
    {
      "label": "Sci-Fi",
      "value": "115"
    },
    {
      "label": "Terror",
      "value": "100"
    },
    {
      "label": "Comedia",
      "value": "30"
    },
    {
      "label": "Drama",
      "value": "30"
    }
  ]
}""")
   return render(request, 'MovieDick_Inicio.html', {'output': chartObj.render()})

def users(request):
   chartObj = FusionCharts( 'sparkwinloss', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "ACTIVIDAD DE USUARIOS",
    "subcaption": "(2020)",
    "charttopmargin": "10",
    "theme": "candy"
  },
  "dataset": [
    {
      "data": [
        {
          "value": "L"
        },
        {
          "value": "L"
        },
        {
          "value": "W"
        },
        {
          "value": "W"
        },
        {
          "value": "W"
        },
        {
          "value": "L"
        },
        {
          "value": "W"
        },
        {
          "value": "L"
        },
        {
          "value": "L"
        },
        {
          "value": "W"
        },
        {
          "value": "W"
        },
        {
          "value": "W"
        },
        {
          "value": "W"
        },
        {
          "value": "L"
        },
        {
          "value": "L"
        },
        {
          "value": "L"
        },
        {
          "value": "L"
        },
        {
          "value": "L"
        },
        {
          "value": "W"
        },
        {
          "value": "L"
        },
        {
          "value": "w"
        },
        {
          "value": "L"
        }
      ]
    }
  ]
}""")
   return render(request, 'usuarios.html', {'output': chartObj.render()})
   
#grafico de busquedas por mes
def chart4(request):
   chartObj = FusionCharts( 'column2d', 'ex1', '500', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Peliculas mas buscadas",
    "subcaption": "",
    "xaxisname": "Pelicula",
    "yaxisname": "busquedas por mes",
    "theme": "Candy"
  },
  "data": [
    {
      "label": "Titanic",
      "value": "350"
    },
    {
      "label": "Mad Max: Fury Road",
      "value": "323"
    },
    {
      "label": "Pulp Fiction",
      "value": "249"
    },
    {
      "label": "El Padrino",
      "value": "208"
    }
  ]
}""")
   return render(request, 'Catalogo.html', {'output': chartObj.render()})

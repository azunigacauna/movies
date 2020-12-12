from django.shortcuts import render
from django.http import HttpResponse

from fusioncharts import FusionCharts
from pprint import pprint
from collections import OrderedDict

def chart(request):
    dataSource = OrderedDict()
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
    chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Country"
    chartConfig["yAxisName"] = "Reserves (MMbbl)"
    chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"

    chartData = OrderedDict()
    chartData["Venezuela"] = 290
    chartData["Saudi"] = 260
    chartData["Canada"] = 180
    chartData["Iran"] = 140
    chartData["Russia"] = 115
    chartData["UAE"] = 100
    chartData["US"] = 30
    chartData["China"] = 30

    dataSource["chart"] = chartConfig
    dataSource["data"] = []
    for key, value in chartData.items():
        dataSource["data"].append({'label':key, 'value': value})

    pprint(dataSource)
    column2D = FusionCharts("column2d", "Oil_Reserves", "600", "400", "Oil_Reserves-container", "json", dataSource)
    context = {'output': column2D.render(), }
    return render(request, 'pag_no_encontrada.html', context)

# Create your views here.
def inicio(request):
    return render(request,'MovieDick_Inicio.html')

def catalogo(request):
    return render(request,'Catalogo.html')

def lista_pelicula(request):
    return render(request,'Lista_Peliculas.html')

def ini_sesion(request):
    return render(request,'inicio_sesion.html')

def perfil(request):
    return render(request, 'Perfil.html')

def resenia(request):
    return render(request, 'Resenia_Pelicula.html')

def registro(request):
    return render(request, 'Registro.html')

def chart2(request):
   chartObj = FusionCharts( 'pie3d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Cantidad de Películas por Género",
    "showvalues": "1",
    "showpercentintooltip": "0",
    "enablemultislicing": "1",
    "theme": "umber"
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
   return render(request, 'categoria.html', {'output': chartObj.render()})


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



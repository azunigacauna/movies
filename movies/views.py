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

def categoria(request):
    return render(request,'Categoria.html')

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

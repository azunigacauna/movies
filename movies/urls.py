"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [

    path('', views.chart3, name='inicio'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path('catalogo', views.chart4, name='catalogo'),
    path('categoria', views.chart2, name='categoria'),
    path('lista_pelicula', views.lista_pelicula, name='lista_pelicula'),
    path('inicio_sesion/', views.ini_sesion, name='ini_sesion'),
    #path('pagina_no_encontrada/', views.pagina_no_encontrada, name='Page not found'),
    path('pagina_no_encontrada/', views.chart, name='Page not found'),
    path('perfil/',views.perfil, name='perfil'),
    path('resenia', views.resenia, name='resenia_pelicula'),
    path('registro', views.registro, name='registro'),
    path('users', views.users, name='users'),
]

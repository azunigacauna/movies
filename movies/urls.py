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

    path('', views.inicio, name='inicio'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path('catalogo', views.catalogo, name='catalogo'),
    path('categoria', views.categoria, name='categoria'),
    path('lista_pelicula', views.lista_pelicula, name='lista_pelicula'),
    path('inicio_sesion/', views.ini_sesion, name='ini_sesion'),
    path('pagina_no_encontrada/', views.pagina_no_encontrada, name='Page not found'),
]

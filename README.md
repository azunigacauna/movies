### Pre-requisitos 📋

_Para la funcionalidad de internacionalizacion, se debe instalar GNU gettext tools para linux se usa el comando_

```
apt-get install gettext
```
_y para windows se descarga desde https://www.gnu.org/software/gettext/

1. Instalación de un Entorno Virtual //
- Se creará una carpeta con el comando:
  - mkdir nombre_de_la_carpeta
- Luego se hará un virtualenv con el comando
- Window:
  - C:\Users\Name\nombre_de_la_carpeta> python -m venv myvenv
- Linux:
- python3 -m venv myvenv
2. Instalacion FrameWork Django
- sudo apt update && sudo apt install python-django
- Instalar Django con Python 3
  - sudo pip3 install django
- Probaremos la versión de Django con:
- django-admin --version 
- Como crear un proyecto;
  - django-admin startproject Movies
- El comando anterior creo una carpeta llamada Movies    
- Con el comando ls:
  - ls Movies/
- Veremos qué archivos se crearon en la carpeta Movies para luego ingresar con:
  - cd Movies y después realizar.
  - python manage.py runserver.
  - Esto nos lanzará un servidor.
- Copiaremos la url en un navegador web y no mostrará un servidor de Django.
3. Internacionalización de datos:
- En nuestro proyecto vamos a nuestro setting.py
- Asimismo colocamos la variable LOCALE_PATHS y defenimos la ruta de la carpeta "locale", el cual       contendrá las carpetas de cada idioma a traducir.
- Definimos en las urls
  - From django.conf.urls import include
  - urlpatterns=[url(r'^i18m/', include('django.conf.urls.i18n'))],
- Luego hacemos el comando 
  - django-admin makemessage -l es 
  - makemessage -l es(dependera del idioma al que quiera traducir el sitio web)
- Luego usamos el comando:
- django-admin compilemessages
- Finalmente en nuestros html usamos:
- {%load i18n%}
- En nuestros templates 
  - Ejemplo
  - {% trans 'Título' %}

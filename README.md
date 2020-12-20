### Pre-requisitos 📋

_Para la funcionalidad de internacionalizacion, se debe instalar GNU gettext tools para linux se usa el comando_

```
apt-get install gettext
```
_y para windows se descarga desde https://www.gnu.org/software/gettext/

_Instalación de un Entorno Virtual //
_Se creará una carpeta con el comando:
_ mkdir nombre_de_la_carpeta
_Luego se hará un virtualenv con el comando
_Window:
_C:\Users\Name\nombre_de_la_carpeta> python -m venv myvenv
_Linux:
_python3 -m venv myvenv
_Instalacion FrameWork Django
_sudo apt update && sudo apt install python-django
_Instalar Django con Python 3
_sudo pip3 install django
_Probaremos la versión de Django con:
_django-admin --version 
_Como crear un proyecto;
_django-admin startproject Movies
_ El comando anterior creo una carpeta llamada Movies    
_ Con el comando ls:
_ ls Movies/
_ Veremos qué archivos se crearon en la carpeta Movies para luego ingresar con:
_ cd Movies y después realizar.
_ python manage.py runserver.
_ Esto nos lanzará un servidor.
_ Copiaremos la url en un navegador web y no mostrará un servidor de Django.
_Internacionalización de datos:
_ En nuestro proyecto vamos a nuestro setting.py
_ Asimismo colocamos la variable LOCALE_PATHS y defenimos la ruta de la carpeta "locale", el cual       contendrá las carpetas de cada idioma a traducir.
_ Definimos en las urls
_ From django.conf.urls import include
_ urlpatterns=[url(r'^i18m/', include('django.conf.urls.i18n'))],
_ Luego hacemos el comando 
_ django-admin makemessage -l es 
_ makemessage -l es(dependera del idioma al que quiera traducir el sitio web)
_ Luego usamos el comando:
_ django-admin compilemessages
_ Finalmente en nuestros html usamos:
_ {%load i18n%}
_En nuestros templates 
_ Ejemplo
_ {% trans 'Título' %}

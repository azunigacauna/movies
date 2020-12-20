from django.contrib import admin

# Register your models here.
from .models import Pelicula, Lista

admin.site.register(Pelicula)
admin.site.register(Lista)

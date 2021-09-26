"""aprendiendoDjango URL Configuration

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
from django.contrib import admin
from django.urls import path

from miapp import views
# import miapp.views tambien funciona
# path('', miapp.views.index, name="index"),
# path('hola-mundo/', miapp.views.hola_mundo, name="hola_mundo"),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('hola-mundo/', views.hola_mundo, name="hola_mundo"),
    path('hola-mundo/<int:redireccion>', views.hola_mundo, name="hola_mundo"),

    path('contacto/', views.contacto, name="contacto"),  # Ruta sin parametros
    path('contacto/<str:nombre>', views.contacto, name="contacto"),  # Con parametros: <tipo:nombre parametro>
    path('contacto/<str:nombre>/<str:apellido>', views.contacto, name="contacto"),  # Dos parametros

    path('crear_articulo/<str:title>/<str:content>', views.crear_articulo, name="crear_articulo"),

    path('obtener_articulo/<int:id>', views.obtener_articulo, name="obtener_articulo"),

    path('editar_articulo/<int:id>/<str:title>/<str:content>', views.editar_articulo, name="editar_articulo"),

    path('obtener_articulos/', views.obtener_articulos, name="obtener_articulos"),

    path('borrar_articulos/<int:id>', views.borrar_articulos, name="borrar_articulos"),

    path('save_article/', views.save_article, name="save_article"),

    path('create_article/', views.create_article, name="create_article"),
]

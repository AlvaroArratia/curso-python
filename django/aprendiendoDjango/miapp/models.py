from django.db import models

# Create your models here.

# Estos modelos van a definir las tablas de la base de datos
# Para indicar que es un modelo de Django se le pasa models.Model a la clase
class Article(models.Model):
    title = models.CharField(max_length=100)  # Es como el varchar
    content = models.TextField()
    # Se agrega un nuevo campo (05-01-2021), se debe repetir el proceso de migracion
    image_url = models.TextField(default='null')  # default='null' guarda un valor nulo por defecto
    public = models.BooleanField()
    # auto_now_add=True guarda la fecha al crear el objeto
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=True guarda la fecha al editar el objeto
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

# Para hacer migraciones
# 1. python manage.py makemigrations -> se obtiene un archivo .py (en la carpeta 
# migrations) con el numero de la migracion y sus datos
# 2. python manage.py sqlmigrate nombre_app numero_migracion
# 3. python manage.py migrate
 
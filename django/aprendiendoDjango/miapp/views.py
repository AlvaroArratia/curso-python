from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q  # para usar OR en consultas

# Create your views here.
# MVC = modelo vista controlador
# MVT = modelo template vista

menu_navegacion = """
    <hr/>
    <h4>Menu navegacion</h4>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/hola-mundo">Hola mundo</a></li>
        <li><a href="/contacto">Contacto</a></li>
    </ul>
    <hr/>
"""

nombres = ['Alvaro', 'Matias']

############Para los formularios############
def save_article():
    articulo = Article(
        "title",
        "content",
        True
    )
    articulo.save()
    return HttpResponse('Articulo creado')


def create_article(request):
    return render(request, 'create_article.html', {
        'title': 'Formulario',
    })
############################################


def index(request):
    # Para vincular templates se usa el metodo render
    return render(request, 'index.html', {
        'title': 'Index',
        'nombres': nombres,
        'variable': 'mmmm'
    })


def hola_mundo(request, redireccion=0):
    if redireccion == 1:
        # 'contacto' hace referencia al parametro nombre de las url
        return redirect('contacto', nombre="Alvaro", apellido="Arratia")
    else:
        return render(request, 'hola_mundo.html')


# Insertando tamplate "hardcodeada"
def contacto(request, nombre="", apellido=""):
    return HttpResponse(menu_navegacion + f"""
        <h1>Contacto {nombre} {apellido}</h1>
    """)


# Trabajando con los datos
def crear_articulo(request, title, content, public=False):
    articulo = Article(
        title,
        content,
        public
    )
    articulo.save()  # Insertar datos en bd
    return HttpResponse('Articulo creado')


def obtener_articulo(request, id):
    try:
        # Obtener registro especifico, agregar parametros para especificar cual (name, pk, title)
        articulo = Article.objects.get(pk=id)
        response = f"Articulo: Nombre: {articulo.title}, Publico: {articulo.public}"
    except Exception as err:
        print(type(err).__name__ + ": " + err)
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)


def editar_articulo(request, id, title, content, public=False):
    try:
        articulo = Article.objects.get(pk=id)
        articulo.title = title
        articulo.content = content
        articulo.public = public
        articulo.save()
        response = "Articulo editado"
    except Exception as err:
        print(type(err).__name__ + ": " + str(err))
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)


def obtener_articulos(request):
    articulos = Article.objects.all()  # Obtiene todos los registros
    # Para obtener los registros ordenados en base a algun atributo
    # usar orderby() y para un orden ascendente o descendente se usa
    # el "-". Ej: Article.objects.all('-title')
    # Para aplicar un limite de registros a mostrar se usa [inicio:final].
    # Ej: Article.objects.all('-title')[0:2]
    return render(request, 'obtener_articulos.html', {
        'title': 'Articulos',
        'articulos': articulos
    })


def buscar_articulos(request):
    # Con filter se puede obtener varios registros que cumplan x condiciones
    articulos = Article.objects.filter(title="alo")
    # Mirar lookups
    # El metodo exclude sirve para excluir registros respecto a alguna 
    # condicion

    # Para usar SQL se puede usar el metodo raw
    # articulos = Article.objects.raw("SQL")

    # Para usar OR en consultas:
    # filter(condicion1 o condicion2)
    # articulos = Article.objects.filter(Q(condicion1) | Q(condicion2))

    return render(request, 'obtener_articulos.html', {
        'title': 'Articulos',
        'articulos': articulos
    })


def borrar_articulos(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('obtener_articulos')

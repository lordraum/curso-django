# Django

## Entorno virtual

### Instalar venv

```bash
pip install virtualenv
```
### Crear entorno virtual
- Crear directorio para el entorno
- Crear entorno

```bash
virtualenv nombre_entorno 
#recomendado usar venv como nombre
```
### Activar entorno virtual

- windows
```bash
source venv\Scripts\activate
```
- linux o macOS
```bash
source venv\bin\activate
```
## Crear proyecto Django

### Instalar Django

```bash
pip install django
```

### Iniciar proyecto django
```bash
django-admin startproject project-name
```

### Ejecutar servidor
```bash
python manage.py run server
```
----------

El archivo *manage.py* ejecuta diferentes funcionalidades de django

### Cambiar puerto por defecto

```bash
python manage.py run server 3000
```

### Crear aplicación
``` bash
python manage.py startapp myapp
```
### Diferencia entre project y app
Un proyecto Django es el contenedor principal que engloba todo el sitio web, mientras que una aplicación Django es una unidad modular que se enfoca en una funcionalidad específica dentro del proyecto.

## Hola mundo en django

### Archivo views.py
contiene el código que define cómo responder a las solicitudes de los usuarios y realizar las acciones necesarias en función de esas solicitudes, como mostrar información, procesar formularios o interactuar con la base de datos, etc.

### Crear función que retorne el mensaje
- Importar Httpresponse
- Definir función => Parámetro request
- return => respuesta http

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello World')
```

### urls.py
contiene las rutas (URLs) del proyecto y especifica qué funciones o clases de vistas se deben llamar para manejar cada URL en particular.

### Definir path e importar función en el projecto
- Ubicarse en el archivo urls.py en el proyecto (mysite)
- Importar función (hello)
```python
from myapp.views import hello
```
- En la función urlPatters => establecer path y funcionalidad a devolver (función hello)

```python
urlpatterns = [
    path("admin/", admin.site.urls), # por defecto en django
    path("", hello),
]
```

## Include

La forma correcta de establecer paths es que cada aplicación maneje su propio archivo urls.py. *include permite importar esos patrones de url en el urls.py del proyecto*

- Importar módulo path y views.py en myapp/urls.py (Aplicación)
- Crear lista urlpatterns, con los paths a añadir.
- Añadir la instrucción *include* en el import del módulo path en mysite/urls.py (proyecto general)
- Agregar en el path con la función *include* con el archivo donde se va a importar los url patterns

```python
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("about/", views.about),
]

```

```python
# mysite/urls.py
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('myapp.urls')),
    # path("home/", include('myapp.urls'))
]
```

## Modelos y bases de datos

### Migraciones
Actualiza la BBDD a partir del código geenrado con python.
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate 
```
------
*Descargar programa DB browser for sqlite para ver la base de datos*

### Modelo
Plantilla, para convertir código de python que será convertido a SQL en una BBDD conectada. Se crean en el archivo *models.py* de cada app.

### Crear modelo
- Importar modulo *models*
- Crear tabla, con una clase (subclase) a partir de *models.Model*
- Establecer columnas => variable (nombre de la columna) => tipo de dato con models.TipoDeDato => max_length

```python
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
```

### Conectar modelos
Ir al archivo settings.py del proyecto (mysite), buscar la lista INSTALLED_APPS, y agregar 'myapp'. Ejecutar el servidor para verificar, hacer migraciones, si se quiere especificando la app. Esto crea el archivo *0001_initial.py* en la carpeta migrations de la app. Ejecutar migraciones especificando la app.
```bash
python manage.py makemigrations myapp
```

### Establecer FK
En la columna que tenga la relación, utilizar el método models.ForeignKey(TablaRelacionada)

#### on_delete
Establece que hacer cuando se borra la base da datos de la que se importa el dato, El valor models.CASCADE elimina todos los datos que tengan relación.

```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete = (models.CASCADE)
```
### Cambiar base de datos conectada a django
- Ir a settings.py lista DATABASES

## Django Shell
Consola que permite interactuar con la BBDD, hacer consultas.

```bash
python manage.py shell 
```

### CREATE

Importar modelos

```python shell
>>> from myapp.models import Project, Task
```
#### Crear instanciando la clase

p = Project(name = "aplicacion movil")

**Importante** => El método save()p = guarda lo creado en la base de datos.

```python shell
>>> p.save()
```

#### model_set

Para establecer un registro también se puede utilizar el nombre de la clase en minúsculas + _ + set

Importar modelos y acceder a un registro (guardarlo en variable).

```python shell
p.task_set.create(title = "desarrollar proyecto 1")
# Se utiliza de esta forma porque así se le llama la modelo en la BBDD
```

### READ

#### método all
Visualiza todos los registros de una base
```python shell
>>> Project.objects.all() # Project es la BBDD
```
#### método get
El método get accede a un registro específico según se indique, ejemplo ID. La búsqueda debe ser exacta.
```python shell
Project.objects.get(id=1)
Project.objects.get(name="aplicacion movil")
```
Para salir del shell se utiliza ctrl + D.

#### model_set
Para acceder a todos los registros se utiliza el método all

```python shell
>>> p.task_set.all()
# Se utiliza de esta forma porque así se le denomina al modelo en BBDD
```

#### filter
Para realizar búsquedas es mejor utilizar el método filter con diferentes opciones de búsqueda.

```python shell
>>> Project.objects.filter(name__startswith="apl")
```

## Url Params

### Definir

En el url pattern

`<tipo-de-dato:parámetro>`
```python
path("hello/<str:username>", views.hello)
```

### Invocar
Definir como parámetro en una vista

```python
def hello(request, username):
    print(username)
    return HttpResponse('Hello World')
    # url/username => en navegador
```

### Renderizar data obtenida en el parámetro
Se utiliza un verbo de formato según el tipo de dato `%s`

```python
return HttpResponse('<h2>Hello %s</h2>' %username)
```

## params and models

### Consultas a través de los params
Importar modelos y JsonResponse en views.py
```python
from .models import import Project, Task
from django.http import HttpResponse, JsonResponse
```

Obtener todos los proyectos en variable

```python
def projects(request):
    projects = Project.objects.all()
    return HttpResponse('projects') 
``` 

Serializar respuesta con JSON response, es necesario agregar el valor `safe=false` en la respuesta y solicitar el queryset (datos de la consulta) como lista. Mostrar los valores de Objects.

```python
def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False) 
```

Otro ejemplo
```python
path("tasks/<int:id>", views.tasks),

def tasks(request, id):
    task = Task.objects.get(id=id)
    return HttpResponse('task: %s' % task.title)
```

### Devolver error 404

Importar modulo de eror 404

```python
from django.shortcuts import get_object_or_404
```

Usar para obtener tarea o devolver error 404
def tasks(request, id):
```python
    def tasks(request, id):
        task = get_object_or_404(Task, id=id)
        return HttpResponse('task: %s' % task.title)
```
## Django Admin

Panel de administrador de django, permite añadir modelos, crear instancias, añadir campos, etc.

```python
path("admin/", admin.site.urls)
# url/admin abre el panel de administrador
```

### admin.py
Permite añadir modelos al panel de administrador.

### Crear usuario
```bash
python manage.py createsuperuser
```

### Añadir modelos a Admin
- Importar modelos en admins.py
- Registrar modelo con `admin.site.register(ModelName)`

### Mostrar los objects en el panel según el campo necesitado
Agregar a la clase modelo un método especificando el tipo de dato y el campo requerido

```python
class Project(models.Model):
    name = models.CharField(max_length=200)    
    def __str__(self):
        return self.name
```

### Concatenar 

## Render
Muestra plantillas html, para generar webs personalizadas y actualizadas.

### Crear plantillas
Crear carpeta templates en la raiz de la app, dónde se guardaran las plantillas en formato html.

### Renderizar template
Importar función `render()` en views
```python
from django.shortcuts import render
```
Devolver la función render con el `request` y el `archivo html` como parámetros

```python
def index(request):
    return render(request, 'index.html')
```

## Templates

### Renderizar datos.
Pasar el dato cómo parámetro de la vista, en un diccionario `{'clave': 'valor'}`

```python
def index(request):
    title = 'Curso de Django'
    return render(request, 'index.html', {'title' : title})
```

## Declarar dato en elemento html
Colocar entre dosbles llaves `{{}}`

```html
<h1>{{title}}</h1>
```
### Template engine
Permiten trabajar con datos en estructuras similares a las de html, que después serán convertidos en html estático. el template engine por defecto de django es jinja 2 (Actualmente jinja 3)

## Jinja - estructuras de control de flujo

[Documentación Jinja](https://jinja.palletsprojects.com/en/3.1.x/)

### jinja loops

bucle for

```python
{% for project in projects %}

<h2>{{project.name}}</h2>

{% endfor %}
```

### jinja condicional if

```python
{% if task.done == False %}
    <p>TAREA PENDIENTE!!!</p>
    {% else %}
    <p>TAREA REALIZADA!!!</p>
    {% endif %}
```

### Condicional if en una línea
```python
<h2>{{task.title}} {% if task.done == False %} ⏰ {% else %} ☑️ {% endif %}</h2>
```

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


















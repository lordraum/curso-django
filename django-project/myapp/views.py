from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask

def index(request):
    title = 'Curso de Django'
    return render(request, 'index.html', {'title' : title})

def about(request):
    return render(request, 'about.html')  

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects' : projects})
  
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks' : tasks})

def create_task(request):
    if request.method == 'GET':            
        return render(request, 'create_task.html', {'form' : CreateNewTask()
        })
    else:          
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)        
        
        return redirect('/tasks/')

def hello(request, username):
    print(username)
    return HttpResponse('<h2>Hello %s</h2>' %username)

def addTaskDescription(id, s):
    tarea_existente = Task.objects.get(id=id)
    tarea_existente.description = s
    tarea_existente.save()

def addTaskDone(id, b):
    tarea_existente = Task.objects.get(id=id)
    tarea_existente.done = b
    tarea_existente.save()
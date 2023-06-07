#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project, Task
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')  

def projects(request):
    return render(request, 'projects.html')
  
def tasks(request):
    return render(request, 'tasks.html')

def hello(request, username):
    print(username)
    return HttpResponse('<h2>Hello %s</h2>' %username)
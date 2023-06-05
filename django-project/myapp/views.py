#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project, Task


def index(request):
    return HttpResponse('Index page')

def hello(request, username):
    print(username)
    return HttpResponse('<h2>Hello %s</h2>' %username)

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False) 

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)
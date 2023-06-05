#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Index page')

def hello(request, username):
    print(username)
    return HttpResponse('<h2>Hello %s</h2>' %username)

def about(request):
    return HttpResponse('About')

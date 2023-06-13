from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Nombre de la tarea', max_length=200) 
    description = forms.CharField(widget=forms.Textarea, label='Describe la tarea')

class CreateNewProject(forms.Form):
    name = forms.CharField(label='título del proyecto', max_length=200)
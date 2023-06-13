from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Nombre de la tarea') 
    description = forms.CharField(widget=forms.Textarea, label='Describe la tarea')
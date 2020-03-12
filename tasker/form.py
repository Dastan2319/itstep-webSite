from django import forms as f

class TaskForm(f.Form):
    text=f.CharField(max_length=10,label='Задача')
    isReady=f.BooleanField(initial=False,label='Ты завершил?',required=False)



from django.shortcuts import render ,redirect
from django.http import HttpResponse ,HttpResponseForbidden
from .models import UserTasks ,User,Task
from django import forms
from django.utils import timezone
# Create your views here.
from .form import TaskForm
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def add(request):
    if request.method == 'GET':
        return render(request,'form_task.html',context=dict(form=TaskForm))
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task=Task(text=form.cleaned_data['text'])
            if form.cleaned_data["isReady"]:
                task.date_complete=timezone.now()
            task.save()
            return redirect(show,task.id)
        else:
            return render(request, 'form_task.html', context=dict(form=form))

def update(request,id:int):
    if request.method == 'GET':
        task=Task.objects.get(id=id)
        isReady=False
        if task.date_complete:
            isReady = True
        else:
            isReady = False

        data={'text':task.text,'isReady':isReady}
        form = TaskForm(data)
        return render(request,'update_task.html',context=dict(form=form))
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.get(id=id)
            task.text=form.cleaned_data['text']
            if form.cleaned_data["isReady"]:
                task.date_complete=timezone.now()
            task.save()
            return redirect(show,task.id)
        else:
            return render(request, 'update_task.html', context=dict(form=form))

def show(request,id:int):
    myTasks=Task.objects.get(id=id)
    return render(request, 'show.html', context=dict(form=myTasks))


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():

            title=form.cleaned_data['title']
        else:
            form = UploadFileForm()
            return render(request, 'files.html', context={'f': form})
        return HttpResponseForbidden('TRUE')
    elif request.method == 'GET':
        # print(data)
        form=UploadFileForm()
        return render(request,'files.html',context={'f':form})
    # return HttpResponseForbidden("Запрещено")
# def new(request):


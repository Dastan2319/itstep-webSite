from django.shortcuts import render
from django.http import HttpResponse
from .models import UserTasks
# Create your views here.
def index(request):
    d=[]
    for i in UserTasks.objects.all():
        d.append({"login":i.user.login,"task":i.task.text})
    data={'tasks':d}
    # print(data)
    return render(request,'index.html',context=data)

# def new(request):

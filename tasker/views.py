from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseForbidden
from .models import UserTasks
from django import forms
# Create your views here.

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
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


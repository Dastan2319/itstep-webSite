from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    d = {
        "foo":"классный",
        'first':1,
        'second':1,
    }
    return render(request,'index.html',context=d)

from django.urls import path
from . import  views

urlpatterns = [
    path('tasker/:int',),
    path('',views.index)
]
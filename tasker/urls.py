from django.urls import path
from . import  views

urlpatterns = [
    path('/index',views.index),
    path('tasker/new',views.add)
]
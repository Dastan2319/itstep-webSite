from django.urls import path
from . import  views

urlpatterns = [
    path('index',views.index),
    path('show/<int:id>', views.show),
    path('update/<int:id>', views.update),
    path('add', views.add),
    # path('tasker/new',views.add)
]
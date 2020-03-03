from django.db import models
from django.db.models import fields as f
# Create your models here.


class User(models.Model):
    login = f.TextField()
    def __str__(self):
        return f'Имя:{self.login}'

class Task(models.Model):
    text=f.TextField(null=False)
    date_add=f.DateTimeField(auto_now_add=True)
    date_complete=f.DateTimeField(blank=True,null=True)
    user_id = models.ForeignKey(User ,on_delete=models.CASCADE)

    def __str__(self):
        return f' Задача №{self.id}  {self.text} '



from django.db import models
from django.db.models import fields as f
# Create your models here.
class Task(models.Model):
    # id=f.IntegerField()
    text=f.TextField(null=False)
    date_add=f.DateTimeField()
    date_complete=f.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f' Задача №{self.id}  {self.text} '

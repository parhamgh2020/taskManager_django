from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=250)
    taskTitle = models.CharField(max_length=250)
    deadline = models.DateField()
    creation_date = models.DateField(auto_now_add=True)

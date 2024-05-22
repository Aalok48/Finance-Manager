from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Expense(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField(default=0)
    category=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField(auto_now_add=True)

    

class Income(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField(default=0)
    source=models.CharField(max_length=35)
    description=models.TextField()
    date=models.DateField(auto_now_add=True)

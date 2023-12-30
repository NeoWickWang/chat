from django.db import models
from datetime import datetime

# Create your models here.

class Account(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=200)
    # id = models.AutoField(primary_key=True)
    # last_login = models.DateTimeField(auto_now_add=True)
    login = models.IntegerField(default=0)  # 0未登录，1登录
    
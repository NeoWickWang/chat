from django.db import models
from datetime import datetime

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=50)
    # members = models.ManyToManyField(Account, blank=True)

    def __str__(self):
        return self.name
    

class Account(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=200)
    # id = models.AutoField(primary_key=True)
    # last_login = models.DateTimeField(auto_now_add=True)
    login = models.IntegerField(default=0)  # 0未登录，1登录
    friend = models.ManyToManyField('self', blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
    
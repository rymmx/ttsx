# coding=utf-8
from django.db import models


class UserInfo(models.Model):
    """定义用户数据库"""
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    udate = models.DateTimeField(auto_now_add=True)
    ushou = models.CharField(max_length=20,default="")
    uadder = models.CharField(max_length=100,default="")
    uyoubian = models.CharField(max_length=6,default="")
    utel = models.CharField(max_length=11,default="")
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.uname.encode("utf-8")

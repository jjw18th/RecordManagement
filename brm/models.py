from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.FloatField()
    publisher=models.CharField(max_length=200)
    def __str__(self):
        return self.title
class BRMuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=200,null=False)

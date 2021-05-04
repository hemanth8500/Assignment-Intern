from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class File(models.Model):
    js = models.FileField(upload_to='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.j

class data(models.Model):
    userId = models.IntegerField(default=1)
    ids = models.IntegerField(default=1)
    title = models.CharField(max_length = 1000)
    body = models.TextField(default="Description")

    def __str__(self):
        return self.userId + " " + self.id
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Parent(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(default=0)

    phone = models.IntegerField(default=0)
    email = models.EmailField()
    babyage = models.IntegerField(default=0)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    parantId = models.IntegerField(default=0)
class Pediatrician(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    PediatricianId = models.IntegerField(default=0)

class Psychologist(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    PsychologistId = models.IntegerField(default=0)


class InformationBoard(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class ExtraInfo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

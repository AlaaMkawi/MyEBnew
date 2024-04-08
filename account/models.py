from django.db import models
from django.contrib.auth.models import User
import datetime


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

class Workshop(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ParentProfile(models.Model):
    parent_name = models.CharField(max_length=100)
    parent_email = models.EmailField(max_length=254)
    parent_phone = models.CharField(max_length=15)
    child_name = models.CharField(max_length=100)
    child_age = models.IntegerField()
    child_gender = models.CharField(max_length=10)
    challenges = models.TextField()

from django.db import models

class Feedback(models.Model):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback - {self.created_at}"

class Comment(models.Model):
    comment_text = models.TextField()  # תיבת טקסט לכתיבת התגובה
    created_at = models.DateTimeField(auto_now_add=True)  # תאריך ושעת השליחה, ייווצרו אוטומטית



class WorkshopSummary(models.Model):
    psychologist_name = models.CharField(max_length=100, default='Anonymous')

    summary_text = models.TextField()
    workshop_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.psychologist_name} - {self.workshop_date}"


class PsychologistSchedule(models.Model):
    workshop_name = models.CharField(max_length=100)
    date = models.DateField()
    hour = models.TimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.workshop_name

class PsychologistComment(models.Model):
    psychologist_name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.psychologist_name} - {self.created_at}"

from django.db import models

class BabyHealth(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name




class ParentInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    def __str__(self):
        return str(self.user)




class PediatricianInfoBoard(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content




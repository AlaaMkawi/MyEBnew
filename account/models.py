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
#SHAHD
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    #age = models.PositiveIntegerField(default=0)  # Set a default value, such as 0
    gender = models.CharField(max_length=10, default='')  # Set a default value, such as an empty string
    child_age = models.PositiveIntegerField(default=0)  # Set a default value, such as 0
    child_gender = models.CharField(max_length=10, default='')  # Set a default value, such as an empty string
    challenges = models.TextField(default='')  # Set a default value, such as an empty string
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Pediatrician(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    PediatricianId = models.IntegerField(default=0)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, default='')  # Set a default value, such as an empty string
    phone_number = models.CharField(max_length=15, default='')  # Set a default value, such as an empty string
    specialization = models.CharField(max_length=100, default='')  # Set a default value, such as an empty string
    experience_years = models.PositiveIntegerField(default=0)  # Set a default value, such as 0
    qualification = models.CharField(max_length=100, default='')  # Set a default value, such as an empty string
    user = models.OneToOneField(User, on_delete=models.CASCADE,default='')

    def __str__(self):
             return f"{self.first_name} {self.last_name}"

class Psychologist(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    PsychologistId = models.IntegerField(default=0)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, default='')  # Set a default value, such as an empty string
    phone_number = models.CharField(max_length=15, default='')  # Set a default value, such as an empty string
    specialization = models.CharField(max_length=100, default='')  # Set a default value, such as an empty string
    experience_years = models.PositiveIntegerField(default=0)  # Set a default value, such as 0
    qualification = models.CharField(max_length=100, default='')  # Set a default value, such as an empty string
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')

    def __str__(self):
             return f"{self.first_name} {self.last_name}"

class InformationBoard(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class ExtraInfo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



from django.db import models

class Feedback(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


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

class PediatricianInfoBoard(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Track(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.parent.name} - {self.parent.parantId} - {self.explanation}"

    @property
    def product_name(self):
        return self.parent.name

    @property
    def product_price(self):
        return self.parent.parantId

class Traking(Parent):
    explanation = models.TextField(blank=True, null=True)

class Paropinion(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username + "'s Profile"


class Workshop(models.Model):
    title = models.CharField(max_length=100)
    day = models.DateField()
    time = models.TimeField()
    link = models.URLField()

class Meeting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    host = models.CharField(max_length=100)




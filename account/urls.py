from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from account import views

urlpatterns = [
    path('', views.index),
    path('loginpsycholist/', views.loginpsycholist, name='loginpsycholist'),
    path('psychomepage/', views.psychomepage, name='psychomepage'),

]

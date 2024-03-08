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

    path('loginpediatrician/', views.loginpediatrician, name='loginpediatrician'),
    path('pedhomepage/', views.pedhomepage, name='pedhomepage'),

    path('loginParent/', views.loginParent, name='loginParent'),
    path('parhomepage/', views.parhomepage, name='parhomepage'),

]
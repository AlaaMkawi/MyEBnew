from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from itertools import count, repeat,chain
from .forms import CreatUserForm

# Create your views here.

def loginpsycholist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Psychologist').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('psychomepage')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'loginpsychologist.html',context)

from django.http import HttpResponse
def index(request):
    return render(request, 'homepage.html')

def psychomepage(request):
    return render(request, 'pyschhomepage.html')

#/-----------------
def loginpediatrician(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='pediatrician').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('pedhomepage')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'loginpediatrician.html',context)

from django.http import HttpResponse
def index(request):
    return render(request, 'homepage.html')

def pedhomepage(request):
    return render(request, 'pedhomepage.html')

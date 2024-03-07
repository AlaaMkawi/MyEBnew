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
#
# def loginAdmin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             users_in_groub = Group.objects.get(name='Admin').user_set.all()
#             if user in users_in_groub:
#                 login(request, user)
#                 return redirect('homepage_admin')
#             else:
#                 messages.info(request, 'Username OR Password incorrert')
#         else:
#             messages.info(request, 'username OR Password incorrert')
#     context = {}
#     return render(request, 'ourproject/log_in_admin.html', context)

from django.http import HttpResponse
def index(request):
    return render(request, 'homepage.html')

def psychomepage(request):
    return render(request, 'pyschhomepage.html')
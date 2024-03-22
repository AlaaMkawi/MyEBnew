from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm
from .forms import ParentSignupForm, CreatUserForm


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
                messages.info(request, 'Username or password incorrect')
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request, 'loginpsychologist.html')

def index(request):
    return render(request, 'homepage.html')

def psychomepage(request):
    return render(request, 'pyschhomepage.html')

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
                messages.info(request, 'Username or password incorrect')
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request, 'loginpediatrician.html')

def pedhomepage(request):
    return render(request, 'pedhomepage.html')

def loginParent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            users_in_group = Group.objects.get(name='Parent').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('parhomepage')
            else:
                messages.info(request, 'Username or password incorrect')
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request, 'loginParent.html')

def parhomepage(request):
    return render(request, 'parhomepage.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def extrainfo(request, extrainfo=None):
    extrainfo = extrainfo.objects.all()
    return render(request, 'extrainfo.html', {extrainfo : extrainfo})

def parenthomepage(request):

    return render(request, 'parenthomepage.html')

def Schedule(request):
    return render(request, 'Schedule.html')
"""def signup(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for Parent ' + user)
            return redirect('loginParent')
"""


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('parhomepage')  # הפנייה לדף הבית של ההורה
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signupys(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('psychomepage')  # הפנייה לדף הבית של ההורה
    else:
        form = UserCreationForm()
    return render(request, 'signupys.html', {'form': form})

def signuped(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('pedhomepage')  # הפנייה לדף הבית של ההורה
    else:
        form = UserCreationForm()
    return render(request, 'signupys.html', {'form': form})

"""def logoutUser(request):
    logout(request)
    return redirect('loginParent')
    """
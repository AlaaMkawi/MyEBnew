'''
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated(view_func):
    def wrapper(request, *args, **kwargs):
         if request.user.is_authenticated:
            return redirect(request, *args, **kwargs)
         else:
             return view_func(request, *args, **kwargs)

    return wrapper
'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from login.models import User_based as User

from login.registration_errors import *
# Create your views here.

def index(request):
    return render(request, 'login/index.html')

def call_login(request):
    user_name = request.POST['user_name'].lower()
    password = request.POST['password']
    
    user = authenticate(request, username=user_name, password=password)
    if user is not None:
        login(request, user)
        public_name = user.public_name
        return render(request, 'login/index.html', {   
            'public_name':      public_name,
            'Is_login':         True,
            'user':             user,
        })
    else:
        return render(request, 'login/index.html', {   
            'user_name':        user_name,
            'error_message':    'Auth failed! (Incorrect log/pass)',
        })

def call_logout(request):
    logout(request)
#     return HttpResponseRedirect(reverse('login:index', kwargs={ 
#     'bye_message':    'See you!'
# }))
    return redirect(reverse('login:index'))

def call_registration(request):
    return render(request, 'login/register.html')

def start_registration(request):
    try:
        public_name = request.POST['public_name']
        user_name = request.POST['user_name'].lower()
        password = request.POST['password']
        user_email = request.POST['user_email']

        check_unique_user_name(user_name)
        check_unique_user_email(user_email)
        check_for_error(user_name, public_name, user_email, password)

        User.objects.create_user(user_name, user_email, public_name, password)

    except Exception as err:
        return render(request, 'login/register.html', {
            'user_name' :       user_name,
            'user_email':       user_email,
            'public_name':      public_name,
            'error_message':    err,
            #add params чтобы заного не вводить
    })
    else:
        return redirect(reverse('login:index'))
    
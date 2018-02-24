from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from login.models import User_based as User
from django.contrib.auth.decorators import login_required

from login.registration_errors import *
# Create your views here.

def user_login(request, original_user_name, password):
    user_name = original_user_name.lower()
    user = authenticate(request, username=user_name, password=password)
    if user is not None:
        login(request, user)
        public_name = user.public_name
        return render(request, 'login/index.html', {   
            'user':             user,
        })
    else:
        return render(request, 'login/index.html', {   
            'user_name':        original_user_name,
            'error_message':    'Auth failed! (Incorrect log/pass)',
        })


def index(request):
    return render(request, 'login/index.html')

def call_login(request):
    original_user_name = request.POST['user_name']
    password = request.POST['password']

    return user_login(request, original_user_name, password)
    

# @login_required(login_url='/login/')
def call_logout(request):
    logout(request)
#     return HttpResponseRedirect(reverse('login:index', kwargs={ 
#     'bye_message':    'See you!'
# }))
    return redirect(reverse('login:index'))


def call_registration(request):
    if not request.user.is_authenticated:
        return render(request, 'login/register.html')
    else:
        return redirect(reverse('home:index'))

def start_registration(request):
    if not request.user.is_authenticated:

        try:
            public_name = request.POST['public_name']
            original_user_name = request.POST['user_name']
            password = request.POST['password']
            original_user_email = request.POST['user_email']

            check_unique_user_name(original_user_name)
            check_unique_user_email(original_user_email)
            check_for_error(original_user_name, public_name, original_user_email, password)

            user = User.objects.create_user(original_user_name, original_user_email, public_name, password)
            user_login(request, original_user_name, password)


        except Exception as err:
            return render(request, 'login/register.html', {
                'user_name' :       original_user_name,
                'user_email':       original_user_email,
                'public_name':      public_name,
                'error_message':    err,
        })
        else:
            return render(request, 'login/change_skills.html', {
                'user':             user,
        })
    else:
        return redirect(reverse('home:index'))

@login_required(login_url='/login/')
def change_skills(request):
    pass

    
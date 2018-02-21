from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'login/index.html')

def call_login(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    user = authenticate(request, username=user_name, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'login/index.html', {   
            'user_name':        user_name,
            'Is_login':    True,
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
    return HttpResponseRedirect(reverse('login:index'))

def call_registration(request):
    return render(request, 'login/register.html')

def start_registration(request):
    try:
        user_name = request.POST['user_name']
        password = request.POST['password']
        user_email = request.POST['user_email']
<<<<<<< HEAD

        User.objects
=======
        password_confirm = request.POST['password_confirm']
        if password != password_confirm:
            raise PasswordConfirmError
            #add error description
>>>>>>> 3bac824e834431fa361387cc1ee12414f6ce1ee7
        user = User.objects.create_user(user_name, user_email, password)
        # user.save()

    except Exception as err:
        return render(request, 'login/register.html', {
            'user_name' :       user_name,
<<<<<<< HEAD
            'error_message':    err,
=======
            'user_email':       user_email,
            'error_message':    'Error (sorry wery vell)',
>>>>>>> 3bac824e834431fa361387cc1ee12414f6ce1ee7
            #add params чтобы заного не вводить
    })
    else:
        #разобраться с передачей параметров при редирректе
        return HttpResponseRedirect(reverse('login:index'))
    
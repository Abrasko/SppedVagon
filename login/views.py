from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from login.models import User_based as User
from django.contrib.auth.decorators import login_required

from login.forms import RegistrationForm
# from login.registration_errors import *
# from login.skillsdict import *

# Create your views here.


def user_login(request, original_user_name, password):
    user_name = original_user_name.lower()
    user = authenticate(request, username=user_name, password=password)
    if user is not None:
        login(request, user)
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


def registration(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                # user = authenticate(request,
                #                     username=form.cleaned_data['user_name'],
                #                     password=form.cleaned_data['password1'],
                #                     )
                # if user is not None:
                login(request, user)
                return redirect('mychar:edit')
        else:
            form = RegistrationForm()

        return render(request, 'login/register.html', {
            'form':     form,
        })

    else:
        return redirect('home:index')


# просто код  - даже еще не запускал
@login_required(login_url='/login/')
def change_skills(request):
    try:
        # есть какой то пост запрос
        # skills_dict - ключ skill_id, уровень скила пользователя
        request_dict = request.POST.dict()
        skills_dict = {}
        user = request.user
        for skill_id in request_dict:
            skills_dict[skill_id] = request_dict[skill_id]

        # user.profileparams_set.create(skills_dict=skills_dict)

    except Exception as err:
        return render(request, 'login/change_skills.html', {
            'user':             user,
            'err':              err
        })
    else:
        return redirect(reverse('mychar:char'))

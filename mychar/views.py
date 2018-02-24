from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from login.models import User_based as User
# Create your views here.

@login_required(login_url='/login/')
def char(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_name = request.user.get_username())
        return render(request, 'mychar/char.html',{
            'user': user,
        })

def user_char(request, user_id):
    return render(request, reverse('mychar:user_char'), {
        'user_id': user_id,
    })
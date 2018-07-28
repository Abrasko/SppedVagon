from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from login.models import User_based as User
from mychar.models import CharPost, CharPhoto
from mychar.forms import (EditProfileForm, EditProfilePasswordForm, AddPostForm,
                          UploadImageForm)
from django.contrib.auth import authenticate, login

from django.utils import timezone

# Create your views here.

# можно не обязательно редирект на логин а показать
# какие то рофлы со вставкой логин меню
# редиректы залупа в 2к18, если юзер перешел туда значит ему надо, а логиниться
# не обязательно на отдельной странице


@login_required(login_url='/login/')
def char(request):
    if request.user.is_authenticated:
        user = User.objects.get(user_name=request.user.get_username())
    # return HttpResponseRedirect(reverse('mychar:user_char',
    #     args=(user.id,)))
    return redirect('mychar:user_char_page', user.id)


def user_char_page(request, user_id):
    user_char = get_object_or_404(User, pk=user_id)
    is_it_own_profile = False
    form = None
    random_users_list = None
    user_char_photo = None
    if request.user.is_authenticated:
        user_viewer = request.user
        if user_viewer == user_char:
            is_it_own_profile = True
            if request.method == 'POST':
                form = AddPostForm(request.POST)
                if form.is_valid():
                    form.save(user_viewer)
                    return redirect('mychar:user_char_page', user_char.id)
            else:
                form = AddPostForm()
# тут наверное будут проверки на доступ по данному юзеру, блеклист итд итп
# когда у нас есть данные по просматриваемому юзеру
# и данные кто смотрит и залогинеен ли он в принципе
    random_users_list = User.objects.order_by('?')[:5]
    user_char_posts = CharPost.objects.filter(
        post_author=user_char).order_by('-post_date')[:10]
    try:
        user_char_photo = CharPhoto.objects.filter(
            photo_author=user_char, is_char_photo=True).order_by('-photo_date')[0]
    except:
        pass
    return render(request, 'mychar/user_char.html', {
        'form':                 form,
        'own_flag':             is_it_own_profile,
        'user_char':            user_char,
        'user_char_id':         user_id,
        'user_char_posts':      user_char_posts,
        'random_users_list':    random_users_list,
        'user_char_photo':      user_char_photo,
    })


@login_required(login_url='/login/')
def edit_char_page(request):
    info_message = None
    error_message = None
    try:
        user = request.user
    except Exception:
        error_message = 'Не удалось получить пользователя'
        return redirect('login:index')
    else:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                info_message = 'Изменения сохранены!'
                return redirect('mychar:user_char_page', user.id)
                # return redirect('mychar:edit')
        else:
            # начальные значения не через initial, а берутся по instance
            # типо джанго дохуя умный вот так вот
            form = EditProfileForm(instance=user)

    return render(request, 'mychar/edit_profile.html', {
        'form':             form,
        'info_message':     info_message,
        'error_message':    error_message,
    })


def edit_password_page(request):
    info_message = None
    error_message = None
    try:
        user = request.user
    except Exception:
        error_message = 'Не удалось получить пользователя'
        return redirect('login:index')
    else:
        if request.method == 'POST':
            form = EditProfilePasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                info_message = 'Пароль успешно изменен!'
                # return redirect('mychar:edit')
        else:
            form = EditProfilePasswordForm(user)

    return render(request, 'mychar/edit_password.html', {
        'error_message': error_message,
        'form': form,
        'info_message': info_message,
    })


def handle_image_file(f, user_name):
    file_path = 'char/' + user_name + '/main.jpg'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_image_page(request):
    info_message = None
    error_message = None
    try:
        user = request.user
    except Exception:
        error_message = "Не удалось получить пользователя(upload_image_page)"
        return redirect("login:index")
    else:
        if request.method == "POST":
            form = UploadImageForm(request.POST, request.FILES)
            if form.is_valid():
                # handle_image_file(request.FILES['image'], user.user_name)
                form.save(user)
                return redirect('mychar:user_char_page', user.id)
        else:
            form = UploadImageForm()

        return render(request, 'mychar/upload_avatar.html', {
            'error_message': error_message,
            'form': form,
            'info_message': info_message,
        })

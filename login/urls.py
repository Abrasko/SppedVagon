from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('call_login/', views.call_login, name='call_login'),
    path('logout/', views.call_logout, name='call_logout'),
    path('registration/', views.registration, name='registration'),
    path('change_skills/', views.change_skills, name='change_skills'),
]
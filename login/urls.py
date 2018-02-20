from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('call_login/', views.call_login, name='call_login'),
    path('logout/', views.call_logout, name='call_logout'),
    path('call_register/', views.call_registration, name='call_registration'),
    path('start_register/', views.start_registration, name='start_registration'),
]
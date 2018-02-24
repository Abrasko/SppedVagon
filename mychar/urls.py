from django.urls import path

from . import views

app_name = 'mychar'
urlpatterns = [
    path('', views.char, name='char'),
    path('<int:user_id>/', views.user_char, name='user_char'),
]
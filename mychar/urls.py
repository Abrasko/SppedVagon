from django.urls import path

from . import views

app_name = 'mychar'
urlpatterns = [
    path('', views.char, name='char'),
    path('<int:user_id>/', views.user_char_page, name='user_char_page'),
    # path('char<int:user_id>/', views.user_char_page, name='user_char_page'),
    path('edit/', views.edit_char_page, name='edit'),
    path('pass/', views.edit_password_page, name='pass'),
    path('upload/', views.upload_image_page, name='upload'),
]

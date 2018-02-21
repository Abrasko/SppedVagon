from django.urls import path, include
from django.views.generic import ListView, DetailView
from blog.models import Post, Comment
from . import views

app_name = 'blog'
urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
    template_name="blog/blog.html")),
    # path('<int:pk>/', DetailView.as_view(model=Post,
    # template_name='blog/post.html')),
    # ex: /polls/
    path('<int:pk>/', views.index, name='index'),
    # path('<int:pk>/', DetailView.as_view(queryset=Comment.objects.all(),
    # template_name="blog/post.html")),
    ]

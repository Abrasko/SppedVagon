from django.shortcuts import render

from .models import Comment, Post

def index(request, pk):
    post = Post.objects.get(id=pk)
    latest_comment_list = post.comment_set.all().order_by("-date")
    context = {'latest_comment_list': latest_comment_list,
                'post': post,
            }
    return render(request, 'blog/post.html', context)
from django.shortcuts import get_object_or_404, render

from .models import Group, Post

COUNT_LAST_POSTS: int = 10


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:COUNT_LAST_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def index(request):
    posts = Post.objects.all()[:COUNT_LAST_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

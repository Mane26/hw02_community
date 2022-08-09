from django.shortcuts import get_object_or_404, render

from .models import Group, Post

COUNT_LAST_POSTS: int = 10
"""Используем переменную константу COUNT_LAST_POSTS,
требуется вывести последние 10 постов."""


def group_posts(request, slug):
    """Страница со списком постов - group_posts,
    отвечающая за запросы, содержимое постов из групп."""
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:COUNT_LAST_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def index(request):
    """Главная страница сайта - index, которая выводит последние 10 постов."""
    posts = Post.objects.all()[:COUNT_LAST_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

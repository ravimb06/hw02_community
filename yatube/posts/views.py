from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = f'Записи сообщества {slug}'
    group = get_object_or_404(Group, slug=slug)
    posts = group.group.all()[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)

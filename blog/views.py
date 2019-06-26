from django.http import Http404
from django.shortcuts import render
from django.views import View
from .models import Post

class PostList(View):
    def get(self, request):
        posts = Post.objects.filter(category__active=True)
        return render(request, 'blog/post-list.html', {"posts_list": posts})


class PostCategory(View):
    def get(self, request, category):
        posts = Post.objects.filter(category__slug=category, category__active=True)
        if posts.existd():
            return render(request, 'blog/post-list.html', {"posts_list": posts})
        else:
            raise Http404


class PostDetail(View):
    """Вывод полной статьи"""
    def get(self, request, id):
        post = Post.objects.get(id=id)
        return render(request, "blog/post-detail.html", context={'post': post})

















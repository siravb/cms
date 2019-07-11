from django.conf import settings
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Post, Comment
from .forms import CommentForm

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
    def get(self, request, category, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm()
        return render(request, "blog/post-detail.html", {'post': post, 'form': form})

    def post(self, request, category, slug):
        #Comment.objects.create(text=request.POST.get("text"), post=Post.objects.get(slug=slug))
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=slug)
            form.user = request.user
            form.save()
            messages.add_message(request, settings.MY_INFO, "Ваш коммент отправлен на проверку ")
        else:
            messages.add_message(request, settings.MY_INFO, "Ошибка")
        return redirect(request.path)

















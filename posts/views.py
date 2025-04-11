from django.shortcuts import render, HttpResponse
from posts.models import Posts
# Create your views here.


def text_view(request):
    return HttpResponse('Porgraming is beatiful!')


def html_view(request):
    return render(request, 'base.html')


def list_view(request):
    posts = Posts.objects.all()
    return render(request, "posts/list_view.html", context={'posts':posts})

def detail_view(request, post_id):  
    post = Posts.objects.get(id=post_id)
    return render(request, 'posts/detail_view.html', context={'post': post})
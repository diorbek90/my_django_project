from django.shortcuts import render, HttpResponse, redirect
from posts.models import Posts
from posts.forms import PostForm, PostForm2
from django.contrib.auth.decorators import login_required
# Create your views here.


def text_view(request):
    return HttpResponse('Porgraming is beatiful!')


def home_page(request):
    return render(request, 'base.html')

@login_required(login_url='/login/')
def list_view(request):
    posts = Posts.objects.all()
    return render(request, "posts/list_view.html", context={'posts':posts})

@login_required(login_url='/login/')
def detail_view(request, post_id):  
    post = Posts.objects.get(id=post_id)
    return render(request, 'posts/detail_view.html', context={'post': post})

@login_required(login_url='/login/') 
def post_create_view(request):

    if request.method == "GET":
        form = PostForm2()  
        return render(request, 'posts/post_create.html', context={'form': form})
    
    if request.method == 'POST':
        
        form = PostForm2(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form':form})
        elif form.is_valid():
            tags = form.cleaned_data.pop('tags')
            post = Posts.objects.create(**form.cleaned_data)
            post.tags.set(tags)
            return redirect('/posts/')



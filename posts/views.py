from django.shortcuts import render, HttpResponse
from posts.models import Posts
from posts.forms import PostForm
# Create your views here.


def text_view(request):
    return HttpResponse('Porgraming is beatiful!')


def home_page(request):
    return render(request, 'base.html')


def list_view(request):
    posts = Posts.objects.all()
    return render(request, "posts/list_view.html", context={'posts':posts})

def detail_view(request, post_id):  
    post = Posts.objects.get(id=post_id)
    return render(request, 'posts/detail_view.html', context={'post': post})


def post_create_view(request):

    if request.method == "GET":
        form = PostForm()

        
            
        return render(request, 'posts/post_create.html', context={'form': form})
    
    if request.method == 'POST':
        
        form = PostForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form':form})
        elif form.is_valid():
            tags = form.cleaned_data.pop('tags')
            post = Posts.objects.create(**form.cleaned_data)
            post.tags.set(tags)
            return render(request, 'posts/detail_view.html', context={'post':post})



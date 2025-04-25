from django.shortcuts import render, HttpResponse, redirect
from posts.models import Posts
from posts.forms import PostForm, PostForm2, SearchForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def text_view(request):
    return HttpResponse('Porgraming is beatiful!')


def home_page(request):
    return render(request, 'base.html')

@login_required(login_url='/login/')
def list_view(request):
    limit = 3
    if request.method == 'GET':
        posts = Posts.objects.all()
        form = SearchForm()
        category_id = request.GET.get('category_id')
        seacrch_q = request.GET.get('search_q')
        ordering = request.GET.get('ordering')
        page = int(request.GET.get('page', 1))
        if category_id:
            posts = posts.objects.filter(category_id=category_id)
        if seacrch_q:
            posts = posts.objects.filter(title__icontains=seacrch_q)
        if ordering:
            posts = posts.order_by(ordering)

        max_pages = posts.count() // limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages)
        elif round(max_pages) == max_pages:
            max_pages = round(max_pages)
        
        start = (page-1) * limit
        end = page * limit
        posts = posts[start:end]
        return render(request,
                       "posts/list_view.html",
                        context={'posts':posts, 'form':form, 'max_pages': range(1, int(max_pages)+1)})

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



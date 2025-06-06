from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Posts
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', context={'form':form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        
        if not form.is_valid():
            return render(request, 'users/register.html', context={'form':form})
        
        elif form.is_valid():
            form.cleaned_data.__delitem__('password_confirm')
            avatar = form.cleaned_data.pop('avatar')
            age = form.cleaned_data.pop('age')
            user = User.objects.create_user(**form.cleaned_data)
            Profile.objects.create(user=user, avatar=avatar, age=age)
            return redirect('/')

def login_view(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', context={'form':form})
    
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if not form.is_valid():
            return render(request, 'users/login.html', context={'form':form})
        elif form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'Invalid username or password')
                return render(request, 'users/login.html', context={'form':form})

@login_required(login_url='/login') 
def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login')  
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    posts = Posts.objects.filter(author=request.user)
    return render(request, 'users/profile.html', context={'profile':profile, 'posts':posts})



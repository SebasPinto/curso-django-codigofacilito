from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterForm

def index(request):
    return render(request, 'index.html', {
        #context
    })


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f'Welcome {user.username}', extra_tags='success')
            return redirect('index')
        else:
            messages.error(request, f'Username or Password is incorrect', extra_tags='danger')
    return render(request, 'users/login.html',{

    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successfuly', extra_tags='info')
    return redirect('login')


def register(request):
    form = RegisterForm(request.POST or None)

    print(request.POST)
    print(form.is_valid())

    if request.method == 'POST' and form.is_valid():
        print('entre a la validacion')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        new_user = User.objects.create_user(username, email, password)

        if new_user:
            login(request, new_user)
            messages.success(request, 'User Created', extra_tags='success')
            return redirect('index')

    return render(request, 'users/register.html',{
        'form':form,

    })

 
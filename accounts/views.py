from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import user_register_form


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            messages.error(request, 'username or password invalid. Try again!')
            
    context = {}
    return render(request, 'login.html', context)


def register(request):

    if request.method == 'POST':
        form = user_register_form(request.POST)
        if form.is_valid():
            form.save()

            usermane = request.POST['username']
            if User:
                user = User.objects.get(username=usermane)
                user.is_staff = True
                user.is_superuser = True
                user.save()
                return redirect('login_page')
    else:
        form = user_register_form() 
    
    context = {'form': form}
    return render(request, 'sign_up.html', context)

def log_out(request):
    logout(request)
    context = {}
    return render(request, 'log_out.html', context)
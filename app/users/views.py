from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('получилось')
            return redirect("home")
        else:
            print('не получилось')
            messages.error(request, "Неверный логин или пароль")

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, 'shop/index.html')


def logout (request):
    return render(request, 'users/logout.html')




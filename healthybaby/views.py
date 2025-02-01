from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('healthybaby:listagem')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'usuarios/login.html')

def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('healthybaby:listagem')
    else:
        form = CustomUserForm()

    return render(request, 'usuarios/register.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def listagem_view(request):
    return render(request, 'listagem.html')
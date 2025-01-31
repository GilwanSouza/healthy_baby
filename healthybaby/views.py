# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente
            return redirect('listagem')  # Redireciona para a página de listagem
    else:
        form = CustomUserForm()

    return render(request, 'usuarios/register.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'usuarios/login.html')
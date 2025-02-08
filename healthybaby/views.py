from django.shortcuts import render, redirect
from .forms import CustomUserForm, GestanteForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Gestante


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

def posParto_view(request):
    return render(request, 'posParto.html')

def consultas_view(request):
    return render(request, 'consultas.html')

def consultaOdonto_view(request):
    return render(request, 'consultaOdonto.html')

def cadastroGestante_view(request):
    return render(request, 'cadastroGestante.html')

def user_logout(request):
    logout(request)
    request.session.flush()
    return redirect('healthybaby:login')

def listar_gestantes(request):
    gestantes = Gestante.objects.all()
    return render(request, 'listagem.html', {'gestantes': gestantes})

def cadastrar_gestante(request):
    if request.method == 'POST':
        form = GestanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_gestantes')
    else:
        form = GestanteForm()
    return render(request, 'cadastroGestante.html', {'form': form})


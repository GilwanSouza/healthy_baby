from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserForm, GestanteForm
from .models import Gestante

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        if not username or not password:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'usuarios/login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('healthybaby:listagem')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'usuarios/login.html')

def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('healthybaby:listagem')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados informados.')
    else:
        form = CustomUserForm()

    return render(request, 'usuarios/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('healthybaby:login')

def index(request):
    return render(request, 'index.html')

def posParto_view(request):
    return render(request, 'posParto.html')

def consultas_view(request):
    return render(request, 'consultas.html')

def consultaOdonto_view(request):
    return render(request, 'consultaOdonto.html')

def listar_gestantes(request):
    gestante = Gestante.objects.all()
    return render(request, 'listagem.html', {'gestantes': gestante})

def cadastrar_gestante(request):
    if request.method == 'POST':
        form = GestanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('healthybaby:listagem')
        else:
            print(form.errors)
            messages.error(request, "Erro ao cadastrar gestante. Verifique os dados informados.")

    else:
        form = GestanteForm()

    return render(request, 'cadastroGestante.html', {'form': form})

def posParto_cadastro(request):
    if request.method == 'POST':
        form = GestanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('healthybaby:listagem')
        else:
            print(form.errors)
            messages.error(request, "Erro ao cadastrar pós-parto. Verifique os dados informados.")
    else:
        form = GestanteForm()

    return render(request, 'posParto.html', {'form': form})


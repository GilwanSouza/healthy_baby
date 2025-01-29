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
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = CustomUserForm()

    return render(request, 'healthybaby/templates/usuarios/register.html', {'form': form})

def index(request):
    return render(request, 'healthybaby/templates/index.html')

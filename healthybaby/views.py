from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserForm, GestanteForm, PosPartoForm, OdontoForm, ConsultaForm
from .models import Gestante, Odonto

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Odonto

def parse_date(date_str):
    from datetime import datetime
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
    except ValueError:
        return None

@csrf_exempt
def salvar_dentes(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            nome_gestante = data.get("nome_gestante", "Paciente Anônimo")
            data_nascimento_gestante = parse_date(data.get("data_nascimento_gestante"))
            cpf_gestante = data.get("cpf_gestante")
            data_consulta = parse_date(data.get("data_consulta"))
            dentes_selecionados = data.get("dentes", [])
            
            if not dentes_selecionados:
                return JsonResponse({"error": "Nenhum dente selecionado"}, status=400)
            
            selecao = Odonto.objects.create(
                nome_gestante=nome_gestante,
                data_nascimento_gestante=data_nascimento_gestante,
                cpf_gestante=cpf_gestante,
                data_consulta=data_consulta,
                dentes_selecionados=dentes_selecionados,
                placa_viavel=data.get("placa_viavel"),
                placa_viavel_data=parse_date(data.get("placa_viavel_data")),
                placa_sangramento=data.get("placa_sangramento"),
                placa_sangramento_data=parse_date(data.get("placa_sangramento_data")),
                placa_sangramento_sondagem=data.get("placa_sangramento_sondagem"),
                placa_sangramento_sondagem_data=parse_date(data.get("placa_sangramento_sondagem_data")),
                calculo_dentario=data.get("calculo_dentario"),
                calculo_dentario_data=parse_date(data.get("calculo_dentario_data")),
                mobilidade=data.get("mobilidade"),
                mobilidade_data=parse_date(data.get("mobilidade_data")),
                perda_insercao=data.get("perda_insercao"),
                perda_insercao_data=parse_date(data.get("perda_insercao_data")),
                plano_tratamento=data.get("plano_tratamento"),
                tratamento_data=parse_date(data.get("tratamento_data")),
                tratamento_dente=data.get("tratamento_dente"),
                procedimento_realizado=data.get("procedimento_realizado"),
                especialidade=data.get("especialidade"),
                tratamento_necessario=data.get("tratamento_necessario"),
                encaminhamento=data.get("encaminhamento"),
                retorno=data.get("retorno"),
                plano_cuidado=data.get("plano_cuidado"),
            )
            
            return JsonResponse({"success": True, "message": "Dentes e informações salvos com sucesso!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método inválido"}, status=400)


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

def cadastrar_consulta(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)

            # Obtém a gestante com segurança
            gestante_id = request.POST.get("gestante_id")
            consulta.gestante = get_object_or_404(Gestante, id=gestante_id)

            consulta.save()
            return redirect("healthybaby:listagem")
    else:
        form = ConsultaForm()

    return render(request, "consultas.html", {"form": form})

def consultaOdontoCadastro(request):
    if request.method == 'POST':
        form = OdontoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('healthybaby:listagem')
        else:
            print(form.errors)
            messages.error(request, "Erro ao cadastrar. Verifique os dados informados.")

    else:
        form = OdontoForm()

    return render(request, 'consultaOdonto.html', {'form': form})

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
        form = PosPartoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('healthybaby:listagem')
        else:
            print(form.errors)
            messages.error(request, "Erro ao cadastrar pós-parto. Verifique os dados informados.")
    else:
        form = PosPartoForm()

    return render(request, 'posParto.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Gestante, PosParto, Odonto, Consulta
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from .models import Gestante, Consulta, Odonto

def detalhes_gestante(request, cpf):
    gestante = get_object_or_404(Gestante, cpf=cpf)
    consultas = Consulta.objects.filter(gestante=gestante)
    consultas_odonto = Odonto.objects.filter(cpf_gestante=cpf)

    return render(request, 'detalhes_gestante.html', {
        'gestante': gestante,
        'consultas': consultas,
        'consultas_odonto': consultas_odonto,
    })

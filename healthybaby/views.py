from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserForm, GestanteForm, PosPartoForm, OdontoForm, ConsultaForm
from .models import Gestante, Odonto
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import Gestante, Odonto, Consulta
from datetime import datetime
from django.contrib.auth.decorators import login_required

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

@login_required
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

@login_required
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

@login_required
def listar_gestantes(request):
    gestante = Gestante.objects.all()
    return render(request, 'listagem.html', {'gestantes': gestante})

@login_required
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

@login_required
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

@login_required
def detalhes_gestante(request, cpf):
    gestante = get_object_or_404(Gestante, cpf=cpf)
    consultas = Consulta.objects.filter(gestante=gestante)
    consultas_odonto = Odonto.objects.filter(cpf_gestante=cpf)

    data_consulta_selecionada = request.GET.get('data_consulta')
    data_odonto_selecionada = request.GET.get('data_odonto')

    consulta_selecionada = None
    consulta_odonto_selecionada = None

    if data_consulta_selecionada:
        try:
            data_formatada = datetime.strptime(data_consulta_selecionada, "%Y-%m-%d").date()
            consulta_selecionada = consultas.filter(data_consulta=data_formatada).first()
        except ValueError:
            pass

    if data_odonto_selecionada:
        try:
            data_formatada = datetime.strptime(data_odonto_selecionada, "%Y-%m-%d").date()
            consulta_odonto_selecionada = consultas_odonto.filter(tratamento_data=data_formatada).first()
        except ValueError:
            pass

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({
            "consulta_selecionada": {
                "data_consulta": consulta_selecionada.data_consulta.strftime("%d/%m/%Y"),
                "observacoes": consulta_selecionada.observacoes or 'N/A',
                "idade_gestacional": str(consulta_selecionada.idade_gestacional) if consulta_selecionada.idade_gestacional else 'N/A',
                "unidade_saude": consulta_selecionada.unidade_saude or 'N/A',
                "especialidade": consulta_selecionada.especialidade or 'N/A',
                "nome_profissional": consulta_selecionada.nome_profissional or 'N/A',
                "crm": consulta_selecionada.crm or 'N/A',
            } if consulta_selecionada else None,
            "consulta_odonto_selecionada": {
                "placa_viavel": consulta_odonto_selecionada.placa_viavel or 'N/A',
                "placa_viavel_data": consulta_odonto_selecionada.placa_viavel_data.strftime("%d/%m/%Y") if consulta_odonto_selecionada.placa_viavel_data else 'N/A',
                "placa_sangramento": consulta_odonto_selecionada.placa_sangramento or 'N/A',
                "placa_sangramento_data": consulta_odonto_selecionada.placa_sangramento_data.strftime("%d/%m/%Y") if consulta_odonto_selecionada.placa_sangramento_data else 'N/A',
                "placa_sangramento_sondagem": consulta_odonto_selecionada.placa_sangramento_sondagem or 'N/A',
                "placa_sangramento_sondagem_data": consulta_odonto_selecionada.placa_sangramento_sondagem_data.strftime("%d/%m/%Y") if consulta_odonto_selecionada.placa_sangramento_sondagem_data else 'N/A',
                "calculo_dentario": consulta_odonto_selecionada.calculo_dentario or 'N/A',
                "calculo_dentario_data": consulta_odonto_selecionada.calculo_dentario_data.strftime("%d/%m/%Y") if consulta_odonto_selecionada.calculo_dentario_data else 'N/A',
                "mobilidade": consulta_odonto_selecionada.mobilidade or 'N/A',
                "mobilidade_data": consulta_odonto_selecionada.mobilidade_data.strftime("%d/%m/%Y") if consulta_odonto_selecionada.mobilidade_data else 'N/A',
                "perda_insercao": consulta_odonto_selecionada.perda_insercao or 'N/A',
                "perda_insercao_data": consulta_odonto_selecionada.perda_insercao_data.strftime("%d/%m/%Y") if consulta_odonto_selecionada.perda_insercao_data else 'N/A',
                "plano_tratamento": consulta_odonto_selecionada.plano_tratamento or 'N/A',
                "tratamento_dente": consulta_odonto_selecionada.tratamento_dente or 'N/A',
                "procedimento_realizado": consulta_odonto_selecionada.procedimento_realizado or 'N/A',
                "especialidade": consulta_odonto_selecionada.especialidade or 'N/A',
                "tratamento_necessario": consulta_odonto_selecionada.tratamento_necessario or 'N/A',
                "encaminhamento": consulta_odonto_selecionada.encaminhamento or 'N/A',
                "retorno": consulta_odonto_selecionada.retorno or 'N/A',
                "plano_cuidado": consulta_odonto_selecionada.plano_cuidado or 'N/A',
            } if consulta_odonto_selecionada else None,
        })

    return render(request, 'detalhes_gestante.html', {
        'gestante': gestante,
        'consultas': consultas,
        'consultas_odonto': consultas_odonto,
        'consulta_selecionada': consulta_selecionada,
        'consulta_odonto_selecionada': consulta_odonto_selecionada,
    })

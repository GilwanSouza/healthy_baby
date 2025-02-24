from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.username

class Gestante(models.Model):
    
    GRAU_PARENTESCO_CHOICES = [
        ('', 'Selecione o Parentesco'),
        ('companheiro', 'Companheiro(a)'),
        ('familiar', 'Familiar'),
        ('amigo', 'Amigo(a)'),
        ('outro', 'Outro'),
    ]
    
    nome = models.CharField(max_length=255, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True, default=None)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    ponto_referencia = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    data_prevista_parto = models.DateField(blank=True, null=True)
    num_sus = models.CharField(max_length=15, blank=True, null=True)
    num_nis = models.CharField(max_length=15, blank=True, null=True)
    nome_social = models.CharField(max_length=255, blank=True, null=True)
    nome_companheiro = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    ocupacao = models.CharField(max_length=255, blank=True, null=True)
    etnia = models.CharField(max_length=55, blank=True, null=True)
    raca = models.CharField(max_length=55, blank=True, null=True)
    
    emg_ctt_nome = models.CharField(max_length=255, blank=True, null=True)
    emg_ctt_telefone = models.CharField(max_length=15, blank=True, null=True)
    emg_ctt_parentesco = models.CharField(max_length=15, choices=GRAU_PARENTESCO_CHOICES, blank=True, null=True)
    
    parceiro_nome = models.CharField(max_length=255, blank=True, null=True)
    parceiro_nome_social = models.CharField(max_length=255, blank=True, null=True)
    parceiro_instrucao = models.CharField(max_length=55, blank=True, null=True)
    parceiro_idade = models.IntegerField(blank=True, null=True)
    parceiro_peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    parceiro_altura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    parceiro_imc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    parceiro_perssaoarterial = models.CharField(max_length=15, blank=True, null=True)
    parceiro_antecedentes = models.CharField(max_length=55, blank=True, null=True)
    parceiro_info = models.CharField(max_length=55, blank=True, null=True)
    
    pcr_exame_abo_data = models.DateField(default=datetime.date.today, blank=True, null=True)
    pcr_exame_abo_resultado = models.CharField(max_length=55, blank=True, null=True)
    pcr_exame_glicemia_data = models.DateField(default=datetime.date.today, blank=True, null=True)
    pcr_exame_glicemia_resultado = models.CharField(max_length=55, blank=True, null=True)
    pcr_exame_hemograma_data = models.DateField(default=datetime.date.today, blank=True, null=True)
    pcr_exame_hemograma_resultado = models.CharField(max_length=55, blank=True, null=True)
    pcr_exame_hiv_data = models.DateField(default=datetime.date.today, blank=True, null=True)
    pcr_exame_hiv_resultado = models.CharField(max_length=55, blank=True, null=True)
    pcr_exame_sifilis_data = models.DateField(default=datetime.date.today, blank=True, null=True)
    pcr_exame_sifilis_resultado = models.CharField(max_length=55, blank=True, null=True)
    pcr_exame_vdrl_data = models.DateField(default=datetime.date.today, blank=True, null=True)
    pcr_exame_vdrl_resultado = models.CharField(max_length=55, blank=True, null=True)
    pcr_exame_hepatite_data = models.DateField(default=datetime.date.today, blank=True, null=True)
    pcr_exame_hepatite_resultado = models.CharField(max_length=55, blank=True, null=True)

    def __str__(self):
        return self.nome
    
class PosParto(models.Model):

    TIPO_NASCIMENTO_CHOICES = [
        ('', 'Selecione o Parentesco'),
        ('prematuro', 'Prematuro'),
        ('atermo', 'A termo'),
    ]

    cpf_mae = models.CharField(max_length=14, blank=True, null=True)

    tipo_parto = models.CharField(max_length=55, blank=True, null=True)
    sangramento = models.CharField(max_length=55, blank=True, null=True)
    medicamentos = models.CharField(max_length=55, blank=True, null=True)
    intercorrencias = models.CharField(max_length=55, blank=True, null=True)
    alta_maternidade = models.CharField(max_length=55, blank=True, null=True)
    peso_alta = models.CharField(max_length=55, blank=True, null=True)
    visita_domiciliar = models.CharField(max_length=55, blank=True, null=True)
    nascimento = models.CharField(max_length=15, choices=TIPO_NASCIMENTO_CHOICES, blank=True, null=True)

    nome_bebe = models.CharField(max_length=55, blank=True, null=True)
    data_nascimento_bebe = models.DateField(blank=True, null=True)
    hora_nascimento_bebe = models.TimeField(blank=True, null=True)
    local_nascimento = models.CharField(max_length=55, blank=True, null=True)
    profissionais = models.CharField(max_length=55, blank=True, null=True)

    def __str__(self):
        return self.nome_bebe
    
class Odonto(models.Model):
    
    ESCOLHA_CHOICES = [
        ('', 'Selecione'),
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    
    cpf_gestante = models.CharField(max_length=14, blank=True, null=True)
 
    placa_viavel = models.CharField(choices=ESCOLHA_CHOICES, max_length=55, blank=True, null=True)
    placa_viavel_data = models.DateField(blank=True, null=True)
    placa_sangramento = models.CharField(choices=ESCOLHA_CHOICES, max_length=55, blank=True, null=True)
    placa_sangramento_data = models.DateField(blank=True, null=True)
    placa_sangramento_sondagem = models.CharField(choices=ESCOLHA_CHOICES, max_length=55, blank=True, null=True)
    placa_sangramento_sondagem_data = models.DateField(blank=True, null=True)
    calculo_dentario = models.CharField(choices=ESCOLHA_CHOICES, max_length=55, blank=True, null=True)
    calculo_dentario_data = models.DateField(blank=True, null=True)
    mobilidade = models.CharField(choices=ESCOLHA_CHOICES, max_length=55, blank=True, null=True)
    mobilidade_data = models.DateField(blank=True, null=True)
    perda_insercao = models.CharField(choices=ESCOLHA_CHOICES, max_length=55, blank=True, null=True)
    perda_insercao_data = models.DateField(blank=True, null=True)
    
    plano_tratamento = models.CharField(max_length=55, blank=True, null=True)
    
    tratamento_data = models.DateField(blank=True, null=True)
    tratamento_dente = models.CharField(max_length=55, blank=True, null=True)
    procedimento_realizado = models.CharField(max_length=55, blank=True, null=True)
    
    especialidade = models.CharField(max_length=55, blank=True, null=True)
    tratamento_necessario = models.CharField(max_length=55, blank=True, null=True)
    encaminhamento = models.CharField(max_length=55, blank=True, null=True)
    retorno = models.CharField(max_length=55, blank=True, null=True)
    plano_cuidado = models.CharField(max_length=55, blank=True, null=True)
    
    def __str__(self):
        return self.nome_gestante
    
class Consulta(models.Model):
    gestante = models.ForeignKey(Gestante, on_delete=models.CASCADE)
    data_consulta = models.DateField()
    observacoes = models.TextField(blank=True, null=True)
    idade_gestacional = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    unidade_saude = models.CharField(max_length=55, blank=True, null=True)
    especialidade = models.CharField(max_length=55, blank=True, null=True)
    nome_profissional = models.CharField(max_length=255, blank=True, null=True)
    crm = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return f"Consulta {self.id} - {self.gestante.nome}"
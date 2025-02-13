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

    TIPO_NASCIMENTO_CHOICES = [
        ('', 'Selecione o Parentesco'),
        ('prematuro', 'Prematuro'),
        ('atermo', 'A termo'),
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

    tipo_parto = models.CharField(max_length=55, blank=True, null=True)
    sangramento = models.CharField(max_length=55, blank=True, null=True)
    medicamentos = models.CharField(max_length=55, blank=True, null=True)
    intercorrencias = models.CharField(max_length=55, blank=True, null=True)
    alta_maternidade = models.CharField(max_length=55, blank=True, null=True)
    peso_alta = models.CharField(max_length=55, blank=True, null=True)
    visita_domiciliar = models.CharField(max_length=55, blank=True, null=True)
    nascimento = models.CharField(max_length=15, choices=TIPO_NASCIMENTO_CHOICES, blank=True, null=True)

    nome_bebe = models.CharField(max_length=55, blank=True, null=True)
    nome_mae = models.CharField(max_length=55, blank=True, null=True)
    data_nascimento_bebe = models.DateField(default=datetime.date.today, blank=True, null=True)
    local_nascimento = models.CharField(max_length=55, blank=True, null=True)
    profissionais = models.CharField(max_length=55, blank=True, null=True)

    def __str__(self):
        return self.nome
    
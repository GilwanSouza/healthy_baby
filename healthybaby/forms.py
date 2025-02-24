from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Gestante, PosParto, Odonto, Consulta
from django.core.exceptions import ValidationError
import re

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        raise ValidationError('CPF inválido. O CPF deve ter 11 dígitos.')

    if cpf == cpf[0] * len(cpf):
        raise ValidationError('CPF inválido. Não use números repetidos.')

    def calcular_dv(cpf, pesos):
        total = sum(int(cpf[i]) * pesos[i] for i in range(len(pesos)))
        resto = total % 11
        return 0 if resto < 2 else 11 - resto

    pesos_primeiro_dv = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo_dv = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    
    primeiro_dv = calcular_dv(cpf, pesos_primeiro_dv)
    segundo_dv = calcular_dv(cpf, pesos_segundo_dv)

    if int(cpf[9]) != primeiro_dv or int(cpf[10]) != segundo_dv:
        raise ValidationError('CPF inválido.')

    return cpf

class CustomUserForm(UserCreationForm):

    data_nascimento = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )
    
    nome = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    
    cpf = forms.CharField(
        label='CPF',
        max_length=14,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF'}),
        validators=[validar_cpf]
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email','nome','data_nascimento', 'telefone', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Digite seu nome de usuário'
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'
        self.fields['data_nascimento'].widget.attrs['placeholder'] = 'Digite sua data de nascimento'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu email'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Digite seu telefone'
        self.fields['password1'].widget.attrs['placeholder'] = 'Digite sua senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua senha'

class GestanteForm(forms.ModelForm):
    nome = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o nome"})
    )

    data_nascimento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Digite a data de nascimento"})
    )

    cpf = forms.CharField(
        required=False,
        max_length=14,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o CPF"})
    )

    telefone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o telefone"})
    )

    endereco = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o endereço"})
    )

    ponto_referencia = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ponto de referência"})
    )

    estado = forms.CharField(
        required=False,
        max_length=2,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Estado"})
    )

    cidade = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Cidade"})
    )

    cep = forms.CharField(
        required=False,
        max_length=9,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "CEP"})
    )

    data_prevista_parto = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Digite a data prevista para o parto"})
    )

    num_sus = forms.CharField(
        required=False,
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Número SUS"})
    )

    num_nis = forms.CharField(
        required=False,
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Número NIS"})
    )

    nome_social = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome social"})
    )

    nome_companheiro = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do companheiro"})
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )

    ocupacao = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ocupação"})
    )

    etnia = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Etnia"})
    )

    raca = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Raça"})
    )

    emg_ctt_nome = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome de contato de emergência"})
    )

    emg_ctt_telefone = forms.CharField(
        required=False,
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Telefone de contato de emergência"})
    )

    emg_ctt_parentesco = forms.ChoiceField(
        required=False,
        choices=[('', 'Selecione o Parentesco'),
        ('companheiro', 'Companheiro(a)'),
        ('familiar', 'Familiar'),
        ('amigo', 'Amigo(a)'),
        ('outro', 'Outro'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    parceiro_nome = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do parceiro"})
    )

    parceiro_nome_social = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome social do parceiro"})
    )

    parceiro_instrucao = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Instrução do parceiro"})
    )

    parceiro_idade = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Idade do parceiro"})
    )

    parceiro_peso = forms.DecimalField(
        required=False,
        max_digits=5, decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Peso do parceiro"})
    )

    parceiro_altura = forms.DecimalField(
        required=False,
        max_digits=5, decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Altura do parceiro"})
    )

    parceiro_imc = forms.DecimalField(
        required=False,
        max_digits=5, decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "IMC do parceiro"})
    )

    parceiro_perssaoarterial = forms.CharField(
        required=False,
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Pressão arterial do parceiro"})
    )

    parceiro_antecedentes = forms.CharField(
        required=False,
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Antecedentes do parceiro"})
    )

    parceiro_info = forms.CharField(
        required=False,
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Informações adicionais sobre o parceiro"})
    )

    pcr_exame_abo_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Data do exame ABO"})
    )

    pcr_exame_abo_resultado = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Resultado do exame ABO"})
    )

    pcr_exame_glicemia_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Data do exame de glicemia"})
    )

    pcr_exame_glicemia_resultado = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Resultado do exame de glicemia"})
    )

    pcr_exame_hemograma_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Data do exame de hemograma"})
    )

    pcr_exame_hemograma_resultado = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Resultado do exame de hemograma"})
    )

    pcr_exame_hiv_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Data do exame HIV"})
    )

    pcr_exame_hiv_resultado = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Resultado do exame HIV"})
    )

    pcr_exame_sifilis_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Data do exame sífilis"})
    )

    pcr_exame_sifilis_resultado = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Resultado do exame sífilis"})
    )

    pcr_exame_vdrl_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Data do exame VDRL"})
    )

    pcr_exame_vdrl_resultado = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Resultado do exame VDRL"})
    )

    pcr_exame_hepatite_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Data do exame hepatite"})
    )

    pcr_exame_hepatite_resultado = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Resultado do exame hepatite"})
    )

    class Meta:
        model = Gestante
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GestanteForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['nome'].widget.attrs['placeholder'] = 'Digite o nome completo'
        self.fields['data_nascimento'].widget.attrs['placeholder'] = 'Selecione a data de nascimento'
        self.fields['cpf'].widget.attrs['placeholder'] = 'Digite o CPF'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Digite o telefone'
        self.fields['endereco'].widget.attrs['placeholder'] = 'Digite o endereço completo'
        self.fields['ponto_referencia'].widget.attrs['placeholder'] = 'Digite o ponto de referência'
        self.fields['estado'].widget.attrs['placeholder'] = 'Digite o estado'
        self.fields['cidade'].widget.attrs['placeholder'] = 'Digite a cidade'
        self.fields['cep'].widget.attrs['placeholder'] = 'Digite o CEP'
        self.fields['data_prevista_parto'].widget.attrs['placeholder'] = 'Selecione a data prevista para o parto'
        self.fields['num_sus'].widget.attrs['placeholder'] = 'Digite o número do SUS'
        self.fields['num_nis'].widget.attrs['placeholder'] = 'Digite o número do NIS'
        self.fields['nome_social'].widget.attrs['placeholder'] = 'Digite o nome social'
        self.fields['nome_companheiro'].widget.attrs['placeholder'] = 'Digite o nome do companheiro'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite o email'
        self.fields['ocupacao'].widget.attrs['placeholder'] = 'Digite a ocupação'
        self.fields['etnia'].widget.attrs['placeholder'] = 'Digite a etnia'
        self.fields['raca'].widget.attrs['placeholder'] = 'Digite a raça'
        
        self.fields['emg_ctt_nome'].widget.attrs['placeholder'] = 'Digite o nome do contato de emergência'
        self.fields['emg_ctt_telefone'].widget.attrs['placeholder'] = 'Digite o telefone de emergência'
        self.fields['emg_ctt_parentesco'].widget.attrs['placeholder'] = 'Digite o parentesco de emergência'
        
        self.fields['parceiro_nome'].widget.attrs['placeholder'] = 'Digite o nome do parceiro'
        self.fields['parceiro_nome_social'].widget.attrs['placeholder'] = 'Digite o nome social do parceiro'
        self.fields['parceiro_instrucao'].widget.attrs['placeholder'] = 'Digite a instrução do parceiro'
        self.fields['parceiro_idade'].widget.attrs['placeholder'] = 'Digite a idade do parceiro'
        self.fields['parceiro_peso'].widget.attrs['placeholder'] = 'Digite o peso do parceiro'
        self.fields['parceiro_altura'].widget.attrs['placeholder'] = 'Digite a altura do parceiro'
        self.fields['parceiro_imc'].widget.attrs['placeholder'] = 'Digite o IMC do parceiro'
        self.fields['parceiro_perssaoarterial'].widget.attrs['placeholder'] = 'Digite a pressão arterial do parceiro'
        self.fields['parceiro_antecedentes'].widget.attrs['placeholder'] = 'Digite os antecedentes do parceiro'
        self.fields['parceiro_info'].widget.attrs['placeholder'] = 'Digite informações adicionais do parceiro'
        
        self.fields['pcr_exame_abo_data'].widget.attrs['placeholder'] = 'Selecione a data do exame ABO'
        self.fields['pcr_exame_abo_resultado'].widget.attrs['placeholder'] = 'Digite o resultado do exame ABO'
        self.fields['pcr_exame_glicemia_data'].widget.attrs['placeholder'] = 'Selecione a data do exame de glicemia'
        self.fields['pcr_exame_glicemia_resultado'].widget.attrs['placeholder'] = 'Digite o resultado do exame de glicemia'
        self.fields['pcr_exame_hemograma_data'].widget.attrs['placeholder'] = 'Selecione a data do exame de hemograma'
        self.fields['pcr_exame_hemograma_resultado'].widget.attrs['placeholder'] = 'Digite o resultado do exame de hemograma'
        self.fields['pcr_exame_hiv_data'].widget.attrs['placeholder'] = 'Selecione a data do exame HIV'
        self.fields['pcr_exame_hiv_resultado'].widget.attrs['placeholder'] = 'Digite o resultado do exame HIV'
        self.fields['pcr_exame_sifilis_data'].widget.attrs['placeholder'] = 'Selecione a data do exame sífilis'
        self.fields['pcr_exame_sifilis_resultado'].widget.attrs['placeholder'] = 'Digite o resultado do exame sífilis'
        self.fields['pcr_exame_vdrl_data'].widget.attrs['placeholder'] = 'Selecione a data do exame VDRL'
        self.fields['pcr_exame_vdrl_resultado'].widget.attrs['placeholder'] = 'Digite o resultado do exame VDRL'
        self.fields['pcr_exame_hepatite_data'].widget.attrs['placeholder'] = 'Selecione a data do exame hepatite'
        self.fields['pcr_exame_hepatite_resultado'].widget.attrs['placeholder'] = 'Digite o resultado do exame hepatite'


class PosPartoForm(forms.ModelForm):

    tipo_parto = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Tipo de parto"})
    )

    sangramento = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Sangramento"})
    )

    medicamentos = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Medicamentos utilizados"})
    )

    intercorrencias = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Intercorrências no parto"})
    )

    alta_maternidade = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Alta da maternidade"})
    )

    peso_alta = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Peso na alta"})
    )

    visita_domiciliar = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Visita domiciliar"})
    )

    nascimento = forms.ChoiceField(
        required=False,
        choices=[('', 'Selecione o tipo de nascimento'),
        ('prematuro', 'Prematuro'),
        ('atermo', 'A termo'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    nome_bebe = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do bebê"})
    )

    data_nascimento_bebe = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Data de nascimento do bebê"})
    )

    local_nascimento = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Local de nascimento"})
    )

    profissionais = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Profissionais envolvidos"})
    )

    cpf_mae = forms.CharField(
        required=False,
        max_length=14,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "CPF da mãe"})
    )

    hora_nascimento_bebe = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={"class": "form-control", "type": "time", "placeholder": "Hora de nascimento do bebê"})
    )

    class Meta:
        model = PosParto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PosPartoForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['cpf_mae'].widget.attrs['placeholder'] = 'Digite o CPF da mãe'

        self.fields['tipo_parto'].widget.attrs['placeholder'] = 'Digite o tipo de parto'
        self.fields['sangramento'].widget.attrs['placeholder'] = 'Digite o sangramento'
        self.fields['medicamentos'].widget.attrs['placeholder'] = 'Digite os medicamentos utilizados'
        self.fields['intercorrencias'].widget.attrs['placeholder'] = 'Digite as intercorrências no parto'
        self.fields['alta_maternidade'].widget.attrs['placeholder'] = 'Digite a alta da maternidade'
        self.fields['peso_alta'].widget.attrs['placeholder'] = 'Digite o peso na alta'
        self.fields['visita_domiciliar'].widget.attrs['placeholder'] = 'Digite a visita domiciliar'
        self.fields['nascimento'].widget.attrs['placeholder'] = 'Selecione o tipo de nascimento'

        self.fields['nome_bebe'].widget.attrs['placeholder'] = 'Digite o nome do bebê'
        self.fields['hora_nascimento_bebe'].widget.attrs['placeholder'] = 'Digite a hora de nascimento do bebê'
        self.fields['data_nascimento_bebe'].widget.attrs['placeholder'] = 'Selecione a data de nascimento do bebê'
        self.fields['local_nascimento'].widget.attrs['placeholder'] = 'Digite o local de nascimento'
        self.fields['profissionais'].widget.attrs['placeholder'] = 'Digite os profissionais envolvidos'
        
class OdontoForm(forms.ModelForm):
    
    nome_gestante = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o nome da gestante"})
    )

    data_nascimento_gestante = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Digite a data de nascimento da gestante"})
    )

    cpf_gestante = forms.CharField(
        required=False,
        max_length=14,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o CPF da gestante"})
    )
    
    placa_viavel = forms.ChoiceField(
        required=False,
        choices=[('', 'Selecione'),
        ('sim', 'Sim'),
        ('nao', 'Não'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    placa_viavel_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Digite a data da placa viável"})
    )
    
    placa_sangramento = forms.ChoiceField(
        required=False,
        choices=[('', 'Selecione'),
        ('sim', 'Sim'),
        ('nao', 'Não'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    placa_sangramento_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Digite a data da placa de sangramento"})
    )
    
    placa_sangramento_sondagem = forms.ChoiceField(
        required=False,
        choices=[('', 'Selecione'),
        ('sim', 'Sim'),
        ('nao', 'Não'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    placa_sangramento_sondagem_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Digite a data da placa de sangramento com sondagem"})
    )
    
    calculo_dentario = forms.ChoiceField(
        required=False,
        choices=[('', 'Selecione'),
        ('sim', 'Sim'),
        ('nao', 'Não'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    calculo_dentario_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Digite a data do cálculo dentário"})
    )
    
    mobilidade = forms.ChoiceField(
        required=False,
        choices=[('', 'Selecione'),
        ('sim', 'Sim'),
        ('nao', 'Não'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    mobilidade_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Digite a data da mobilidade"})
    )
    
    perda_insercao = forms.ChoiceField(
        required=False,
        choices=[('', 'Selecione'),
        ('sim', 'Sim'),
        ('nao', 'Não'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    perda_insercao_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Digite a data da perda de inserção"})
    )
    
    tratamento_data = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Digite a data do tratamento"})
    )
    
    tratamento_dente = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o dente tratado"})
    )
    
    procedimento_realizado = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o procedimento realizado"})
    )
    
    especialidade = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite a especialidade"})
    )
    
    tratamento_necessario = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o tratamento necessário"})
    )
    
    encaminhamento = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o encaminhamento"})
    )
    
    retorno = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o retorno"})
    )
    
    plano_cuidado = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o plano de cuidado"})
    )
    
    class Meta:
        model = Odonto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OdontoForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['nome_gestante'].widget.attrs['placeholder'] = 'Digite o nome da gestante'
        self.fields['cpf_gestante'].widget.attrs['placeholder'] = 'Digite o CPF da gestante'
        self.fields['data_nascimento_gestante'].widget.attrs['placeholder'] = 'Selecione a data de nascimento da gestante'
        
        self.fields['placa_viavel'].widget.attrs['placeholder'] = 'Selecione a placa viável'
        self.fields['placa_viavel_data'].widget.attrs['placeholder'] = 'Digite a data da placa viável'
        self.fields['placa_sangramento'].widget.attrs['placeholder'] = 'Selecione a placa de sangramento'
        self.fields['placa_sangramento_data'].widget.attrs['placeholder'] = 'Digite a data da placa de sangramento'
        self.fields['placa_sangramento_sondagem'].widget.attrs['placeholder'] = 'Selecione a placa de sangramento com sondagem'
        self.fields['placa_sangramento_sondagem_data'].widget.attrs['placeholder'] = 'Digite a data da placa de sangramento com sondagem'
        self.fields['calculo_dentario'].widget.attrs['placeholder'] = 'Selecione o cálculo dentário'
        self.fields['calculo_dentario_data'].widget.attrs['placeholder'] = 'Digite a data do cálculo dentário'
        self.fields['mobilidade'].widget.attrs['placeholder'] = 'Selecione a mobilidade'
        self.fields['mobilidade_data'].widget.attrs['placeholder'] = 'Digite a data da mobilidade'
        self.fields['perda_insercao'].widget.attrs['placeholder'] = 'Selecione a perda de inserção'
        self.fields['perda_insercao_data'].widget.attrs['placeholder'] = 'Digite a data da perda de inserção'
        
        self.fields['plano_tratamento'].widget.attrs['placeholder'] = 'Digite o plano de tratamento'
        
        self.fields['tratamento_data'].widget.attrs['placeholder'] = 'Digite a data do tratamento'
        self.fields['tratamento_dente'].widget.attrs['placeholder'] = 'Digite o dente tratado'
        self.fields['procedimento_realizado'].widget.attrs['placeholder'] = 'Digite o procedimento realizado'
        
        self.fields['especialidade'].widget.attrs['placeholder'] = 'Digite a especialidade'
        self.fields['tratamento_necessario'].widget.attrs['placeholder'] = 'Digite o tratamento necessário'
        self.fields['encaminhamento'].widget.attrs['placeholder'] = 'Digite o encaminhamento'
        self.fields['retorno'].widget.attrs['placeholder'] = 'Digite o retorno'
        self.fields['plano_cuidado'].widget.attrs['placeholder'] = 'Digite o plano de cuidado'
        
class ConsultaForm(forms.ModelForm):

    gestante = forms.ModelChoiceField(
        queryset=None,  # Deve ser definido no __init__
        required=False,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    data_consulta = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Data da consulta"})
    )

    observacoes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Observações"})
    )

    idade_gestacional = forms.DecimalField(
        required=False,
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Idade gestacional (semanas)"})
    )

    unidade_saude = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Unidade de saúde"})
    )

    especialidade = forms.CharField(
        required=False,
        max_length=55,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Especialidade médica"})
    )

    nome_profissional = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do profissional"})
    )
    
    crm = forms.CharField(
        required=False,
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "CRM do profissional"})
    )

    class Meta:
        model = Consulta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)

        self.fields['gestante'].queryset = Consulta.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['gestante'].widget.attrs['placeholder'] = 'Selecione a gestante'
        self.fields['data_consulta'].widget.attrs['placeholder'] = 'Selecione a data da consulta'
        self.fields['observacoes'].widget.attrs['placeholder'] = 'Digite observações adicionais'
        self.fields['idade_gestacional'].widget.attrs['placeholder'] = 'Digite a idade gestacional'
        self.fields['unidade_saude'].widget.attrs['placeholder'] = 'Digite a unidade de saúde'
        self.fields['especialidade'].widget.attrs['placeholder'] = 'Digite a especialidade médica'
        self.fields['nome_profissional'].widget.attrs['placeholder'] = 'Digite o nome do profissional'
        self.fields['crm'].widget.attrs['placeholder'] = 'Digite o CRM do profissional'
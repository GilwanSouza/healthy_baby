from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Gestante
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
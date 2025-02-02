from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
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

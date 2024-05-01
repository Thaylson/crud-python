from django.forms import ModelForm
from app.models import Pessoa



class Pessoaform(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['Nome', 'CPF', 'Email']
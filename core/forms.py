# coding=utf-8
from django import forms
topic = (
    (1,("Postagem")),
    (2,("Produto")),
    (3,("Projeto")),
    (4,("Duvida")),
    (5,("Outros")),
    (6,("Orçamento"))
)
class Contact(forms.Form):
    name    = forms.CharField(label='Nome',max_length=100,
    widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Digite o Nome Aqui'}))
    email   = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Digite o Email Aqui'}))
    message = forms.CharField(label='Menssagem',widget=forms.Textarea(attrs={'class' : 'form-control','placeholder': 'Deixe o Recado Aqui'}))
    option  = forms.ChoiceField(choices=topic, label="Tópico",initial ="Postagem",widget=forms.Select())
    file = forms.FileField(label='Entre com a Inspiração')

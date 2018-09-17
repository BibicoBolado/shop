# coding=utf-8
from django import forms
from django.core.mail import send_mail
from django.conf import settings

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
    file = forms.FileField(label='Entre com a Inspiração',required=False)
    def sendMail(self,name,email,message,option):
        subject = 'Contato Blog %s' %name
        message = 'Nome: %s; Email: %s; Mensagem: %s; Opção: %s' %(name,email,message,option)
        send_mail(subject,message,settings.EMAIL_HOST_USER ,[settings.CONTACT_EMAIL])

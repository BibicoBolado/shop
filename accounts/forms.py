# coding=utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    username    =   forms.CharField(label = 'Usuario',max_length=100,
                    widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Login'}))
    email       =   forms.EmailField(max_length=254,
                    widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Email'}))
    password1   =   forms.CharField(label = 'Senha',max_length=32, 
                    widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder': 'Senha'}))
    password2   =   forms.CharField(label = 'Confirmação Senha',max_length=32, 
                    widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder': 'Senha'}))

    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já Existe Usuario com Esse email')
        return email

    def save(self,commit=True):
        user=super(RegisterForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields  =   ('name','cep','address','number','uf','complemento','cidate','bairro')
        widgets = {
            'birthday': forms.TextInput(attrs={"type":"date"}),
        }


class Login(forms.Form):
    usernameLogin    =   forms.CharField(label = 'Login ou Email',max_length=100,
    widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Login'}))

    passwordLogin = forms.CharField(label='Senha',max_length=32, 
    widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder': 'Senha'}))
# coding=utf-8
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import Login,RegisterForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def entry(request):
    template_name    = 'login.html'
    context          = {}
    form             = Login()
    form2            = RegisterForm()
    context['form']  = form
    context['form2'] = form2
    return render(request,template_name,context)

def log(request):
    context         = {}
    if request.method=='POST':
        form = Login(request.POST)
        if form.is_valid():
            context['is_valid']=True
         
            username = form.cleaned_data['usernameLogin']
            password = form.cleaned_data['passwordLogin']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user, backend='accounts.backends.ModelBackend')
                return redirect('checkout:cart_view')
            else:
                print(user)
                messages.warning(request, 'Usuário ou Senha Invalidos')
                return redirect('accounts:login')
        else:
                messages.warning(request, 'Usuário ou Senha Invalidos')
                return redirect('accounts:login')
    else:
        pass

def reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user=authenticate(
                username=user.username,
                password=form.cleaned_data['password1']
                )
            login(request,user)
            messages.success(request,('Você pode terminar seu cadastro quando quiser'))
            return redirect('accounts:update_profile')
        else:
            print(form.errors )
            messages.warning(request, form.errors)
            return redirect('accounts:login')
    else:
        pass

@login_required
def data(request):
    
    template_name = 'data.html'
    return render(request,template_name)

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            for field in profile_form.changed_data:
                if field == 'name':
                    request.user.profile.name = profile_form.cleaned_data[field]
                elif field == 'birthday':
                    request.user.profile.birthday = profile_form.cleaned_data[field]
                print(field)
                print(profile_form.cleaned_data[field])
            request.user.profile.save()
            messages.success(request,('Perfil Atualizado com Sucesso!'))
            return redirect('accounts:data')
        else:
            messages.error(request,('ERRO!'))
    else:
        profile_form = ProfileForm()
    return render(request, 'changeprofile.html', {
        'profile_form': profile_form
    })

@login_required
def out(request):
    logout(request)
    messages.success(request, 'Sessão Encerrada')
    return redirect('accounts:login')
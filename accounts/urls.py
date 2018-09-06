# coding=utf-8
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import logout
from .import views

app_name='accounts'
urlpatterns=[
    path('',views.entry,name='login'),
    path('entrar/',views.log,name='log'),
    path('registrar/',views.reg,name='reg'),
    path('dados/',views.data,name='data'),
    path('dados/atualizar/',views.update_profile,name='update_profile'),
    path('sair/',views.out,name='logout'),


]
# coding=utf-8
from django.urls import path
from .import views


app_name='core'
urlpatterns=[
    #paginas iniciais
    path('',views.index,name='index'),
    path('contato',views.contact,name='contact'),
    path('portifolio',views.portifolio,name='portifolio'),
    path('loja',views.shop,name='shop'),
    path('blog',views.blog,name='blog'),
    #paginas de categorias
    path('loja/categoria/<slug:slug>',views.categoryShop,name='categoryShop'),
    path('blog/categoria/<slug:slug>',views.categoryBlog,name='categoryBlog'),
    path('portifolio/categoria/<slug:slug>',views.categoryCatalog,name='categoryCatalog'),
    #paginas de itens individuais
    path('loja/<slug:slug>',views.itenShop,name='itenShop'),
    path('blog/<slug:slug>',views.itenBlog,name='itenBlog'),
    path('portifolio/<slug:slug>',views.itenPortifolio,name='itenPortifolio'),
    #Favoritando Projeto
    path('portifolio/favoritar/',views.favoriteProject,name='favoriteProject'),

]
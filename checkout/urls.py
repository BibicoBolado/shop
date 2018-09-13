# coding=utf-8
from django.urls import path
from .import views

app_name='checkout'
urlpatterns=[
    path('carrinho/adicionar/<slug:slug>',
    views.create_cartitem,name='create_cartitem'),
    path('carrinho/',views.cart_view,name='cart_view'),
    path('finalizar-compra/',views.checkout,name='checkout'),
    path('finalizar-compra/<int:pk>/pagseguro/',views.pagseguro_view,name='pagseguro_view'),
    path('meus-pedidos/',views.order_list,name='order_list'),
    path('meus-pedidos/<int:pk>/',views.order_detail,name='order_detail'),
    path('notificacoes/',views.pagseguro_notification,name='pagseguro_notification'),
    path('frete/',views.frete,name='frete'),
    path('favoritos/',views.favorites,name='favorites'),
]
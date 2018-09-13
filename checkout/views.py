# coding=utf-8
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import RedirectView, TemplateView,ListView,DetailView
from django.contrib import messages
from shop.models import Product
from .models import CartIten,Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
from pagseguro import PagSeguro
from django.db.models import Q


def favorites(request):
    template_name = 'favorites.html'
    return render (request,template_name)

class CreateCartItemView(RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        product     = get_object_or_404(
                     Product,slug=self.kwargs['slug']
                    )
        if self.request.session.session_key is None:
            self.request.session.save()
            print(self.request.session.session_key)
        cart_iten,created   = CartIten.objects.add_item(
                    self.request.session.session_key,
                    product
                      )
        if created:
            messages.success(self.request,'Produto Adicionado Com Sucessos')
        else:
             messages.success(self.request,'Quantidade Atualizada')

        return reverse('checkout:cart_view')

create_cartitem = CreateCartItemView.as_view()

class CartView(TemplateView):

    template_name   =  'cart.html'

    def get_formset(self,clear=False):
        CartItenFormSet = modelformset_factory(CartIten,
        fields=('quantity',),can_delete=True,extra=0)

        session_key = self.request.session.session_key

        if session_key:
            if clear:
                formset=CartItenFormSet(
                queryset=CartIten.objects.filter(cart_id=session_key))
            else:
                formset=CartItenFormSet(
                queryset=CartIten.objects.filter(cart_id=session_key), 
                data=self.request.POST or None)
        else:
            formset=CartItenFormSet(queryset=CartIten.objects.none())
        return formset

    def get_context_data(self,**kwargs):
        context = super(CartView,self).get_context_data(**kwargs)
        context['formset']          =   self.get_formset()
        context['peso']             =   settings.PESO_PLANNER
        context['comprimento']      =   settings.COMPRIMENTO
        context['largura']          =   settings.LARGURA
        context['altura']           =   settings.ALTURA
        context['origem']           =   settings.CEP_ORIGEM
        context['formato']          =   settings.FORMATO

        return context

    def post(self,request,*args,**kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request,'Carrinho Atualizado com Sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)
cart_view = CartView.as_view()


class CheckoutView(LoginRequiredMixin,TemplateView):
    template_name = 'checkout.html'
    login_url = "/usuario/"
    def get(self, request, *args, **kwargs):
        response = super(CheckoutView, self).get(request, *args, **kwargs)
        order = Order.objects.last()
        response.context_data['order'] = order
        return response
checkout = CheckoutView.as_view()

class OrderListView(LoginRequiredMixin,ListView):
    template_name='order_list.html'
    def get_queryset(self):
        return Order.objects.filter(Q(user=self.request.user,status=1) | Q(user=self.request.user,status=3) )

order_list = OrderListView.as_view()

class OrderDetailView(LoginRequiredMixin,DetailView):
    template_name = 'order_detail.html'
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

order_detail = OrderDetailView.as_view()

class PagSeguroView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        order_pk = self.kwargs.get('pk')
        order = get_object_or_404(
            Order.objects.filter(user=self.request.user), pk=order_pk
        )
        pg = order.pagseguro()
        pg.redirect_url = self.request.build_absolute_uri(
            reverse('checkout:order_detail', args=[order.pk])
        )
        #pg.redirect_url = 'www.google.com.br'
        pg.notification_url = self.request.build_absolute_uri(
            reverse('checkout:pagseguro_notification')
        )
        response = pg.checkout()
        #print(dir(response))
        #print(response.code)
        print('##########################################################################')
        print(response.xml)
        print('##########################################################################')
        
        return response.payment_url

pagseguro_view = PagSeguroView.as_view()

@csrf_exempt
def pagseguro_notification(request):
    notification_code = request.POST.get('notificationCode', None)
    if notification_code:
        pg = PagSeguro(
            email=settings.PAGSEGURO_EMAIL, token=settings.PAGSEGURO_TOKEN,
            config={'sandbox': settings.PAGSEGURO_SANDBOX}
        )
        notification_data = pg.check_notification(notification_code)
        status = notification_data.status
        reference = notification_data.reference
        try:
            order = Order.objects.get(pk=reference)
        except Order.DoesNotExist:
            pass
        else:
            order.pagseguro_update_status(status)
    return HttpResponse('OK')
    
@csrf_exempt
def frete(request):
    if request.is_ajax():
        resquest_data = request.POST
        a=list(resquest_data.items())
        frete=a[0][1] #valor
        prazo=a[1][1] #prazo
        session_key = request.session.session_key
        if session_key and CartIten.objects.filter(cart_id=session_key).exists():
            messages.info(request, 'Finalize sua Compra')
            cart_items = CartIten.objects.filter(cart_id=session_key)
            order = Order.objects.create_order(
                user=request.user, cart_itens=cart_items,
                frete=frete,prazo=prazo
            )
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('checkout:cart_view')
    return HttpResponse('OK')
    
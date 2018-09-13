# coding=utf-8
from pagseguro import PagSeguro
from django.db import models
from django.conf import settings
from shop.models import Product
# Create your models here.

class CartItenManager(models.Manager):

    def add_item(self,key,product):
        #VERIFICA SE JA HÁ O ITEM NO CARRINHO SE HOUVER ELE ADICIONA MAIS 1
        if self.filter(cart_id = key,product=product).exists():
            created = False
            cart_item = self.get(cart_id=key,product=product)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartIten.objects.create(
                cart_id = key, product=product,price=product.price
            )
        return cart_item,created
        

class CartIten(models.Model):
    cart_id     = models.CharField('Chave do Carrinho',max_length=40,
                db_index=True,null=True)
    product     = models.ForeignKey('shop.Product',verbose_name='Produto',on_delete='CASCADE')
    quantity    = models.PositiveIntegerField('Quantidade',default=1)
    price       = models.DecimalField('Preço',decimal_places=2,max_digits=8)

    objects = CartItenManager()
    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together=(('cart_id','product'),)
    def __str__(self):
        return '{} {}'.format(self.product,self.quantity)

class OrderManager(models.Manager):
    def create_order(self,user,cart_itens,frete,prazo):
        order = self.create(user=user,frete=frete,prazo=prazo)
        for cart_iten in cart_itens:
            order_iten = OrderIten.objects.create(
                order=order,quantity=cart_iten.quantity,product=cart_iten.product,
                price=cart_iten.price
            )
        return order
        

class Order(models.Model):
    STATUS_CHOICES = (
        (0,'Aguardando Pagamento'),
        (1,'Compra Concluida'),
        (2,'Compra Cancelada'),
        (3,'Está Chegando!'),
    )
    PAYMENT_OPTIONS_CHOICES = (
        ('pagseguro','PagSeguro'),
        ('paypal','Paypal'),
        ('boleto','Boleto')
    )



    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete='CASCADE',verbose_name='Usuário')
    status = models.IntegerField(
        'Situação',choices=STATUS_CHOICES,default=0,blank=True)
    payment_option = models.CharField(
        'Opção de Pagamento',choices=PAYMENT_OPTIONS_CHOICES,default='pagseguro',blank=True,max_length=20)


    created = models.DateTimeField('Criado em',auto_now_add=True)
    modified= models.DateTimeField('Atualizado em', auto_now=True)


    frete       = models.FloatField('Valor Frete',blank=True,null=True)
    prazo       = models.IntegerField('Prazo Entrega',blank=True,null=True)
    rastreio    = models.CharField('Código Rastreio',blank=True,null=True,max_length=100)


    objects = OrderManager()
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural='Pedidos'
    def __str__(self):
        return 'Pedido #{}'.format(self.pk)

    def products(self):
        products_ids = self.Itens.values_list('product')
        return Product.objects.filter(pk__in=products_ids)
    
    def total(self):
         aggregate_queryset = self.Itens.aggregate(
             total=models.Sum(
                 models.F('price')*models.F('quantity'),output_field=models.DecimalField()
             )
         )
         return aggregate_queryset['total']

    def totalCompra(self):
        return self.frete + float(self.total())
    
    def pagseguro_update_status(self, status):
        if status == '3':
            self.status = 1
        elif status == '7':
            self.status = 2
        self.save()
    
    def pagseguro(self):

        pg = PagSeguro(
            email=settings.PAGSEGURO_EMAIL, token=settings.PAGSEGURO_TOKEN,
            config={'sandbox': settings.PAGSEGURO_SANDBOX}
        )
        pg.sender = {
            'email': self.user.email
        }
        pg.extra_amount = '%.2f' % self.frete
        print(self.frete)
        pg.reference_prefix = ''
        pg.shipping = None
        pg.reference = self.pk
        for iten in self.Itens.all():
            pg.items.append(
                {
                    'id': iten.product.pk,
                    'description': iten.product.name,
                    'quantity': iten.quantity,
                    'amount': '%.2f' % iten.price
                }
            )

        return pg
        

class OrderIten(models.Model):
    order       = models.ForeignKey(Order,verbose_name='Pedido',related_name='Itens',on_delete='CASCADE')
    product     = models.ForeignKey('shop.Product',verbose_name='Produto',on_delete='CASCADE')
    quantity    = models.PositiveIntegerField('Quantidade',default=1)
    price       = models.DecimalField('Preço',decimal_places=2,max_digits=8)

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens dos Pedidos'
    def __str__(self):
        return '#{} {} '.format(self.order,self.product)

def post_save_cart_iten(instance,**kwargs):
    if instance.quantity < 1:
        instance.delete()

models.signals.post_save.connect(
    post_save_cart_iten,sender = CartIten, dispatch_uid='post_save_cart_iten'
)
#post_Save determinar que vai ser chamado após salvar algum model
#sender indica que só vai chamar a função depois de salvar um
#cartiten e nenhum outro model daqui
#toda vez que um modelo de cartiten for salvo ele fai chamar
# a função post_save_cart_iten por causa do codigo     acima
# isso SÃO OS signals do DJANGO
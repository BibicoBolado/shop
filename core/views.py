# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .forms import Contact
from shop.models import Product,CategoryShop
from blog.models import Post,CategoryBlog
from catalog.models import Image,Project,CategoryCatalog

#### HOME E CONTATO ####

def index(request):
    template_name       ='core/index.html'
    return render(request,template_name)

def contact(request):
    template_name       = 'contact.html'
    context             = {}
    form                = Contact()

    context['form']     =form
    return render(request,template_name,context)
#### FIM HOME E CONTATO ####

##### LISTAGENS INDEX #####

def portifolio(request):

    category            = CategoryCatalog.objects.all()
    project             = Project.objects.all()
    context             = {}

    context['project']  = project
    context['category'] = category


    template_name='portifolio.html'
    return render(request,template_name,context)

class ProductListView(ListView):
    template_name='product_list.html'
    #context_object_name= 'products'
    #se eu não usar o código a cima
    # o padrão será    product_list
    def get_queryset(self):
        #self.request - requisição
        #self.kwargs - argumentos nomeados
        #self.args - argumentos não nomeados da url
        product = Product.objects.all()
        return product

    def get_context_data(self,**kwargs):
        context = super(ProductListView,self).get_context_data(**kwargs)
        context['destaque']=Product.objects.filter(featured=2)
        context['category']=CategoryShop.objects.all()
        return context
    #com a função acima eu posso colocar quantos contextos quiser dentro da minha listview
shop=ProductListView.as_view()

#def shop(request):
#
#    category            =CategoryShop.objects.all()
#    product             =Product.objects.filter(featured=1)
#    destaque            =Product.objects.filter(featured=2)
#
#
#    context             ={}
#    context['category'] =category
#    context['product']  =product
#    context['destaque'] =destaque
#
#
#    template_name='product_list.html'
#    return render(request,template_name,context)

def blog(request):
    
    category           = CategoryBlog.objects.all()
    postbot            = Post.objects.all()
    context={}

    context['category'] =    category
    context['postbot']  =    postbot

    template_name       = 'post_list.html'
    return render(request,template_name,context)
##### FIM LISTAGENS INDEX#####

##### LISTAGEM DE CATEGORIAS #####
def categoryShop(request,slug):
    
    category = CategoryShop.objects.get(slug=slug)
    product  = Product.objects.filter(category=category)
    context             = {}
    context['category'] = category
    context['product']  = product
    template_name       = 'category.html'
    return render(request,template_name,context)

def categoryBlog(request,slug):
    category            =   CategoryBlog.objects.get(slug=slug)
    postbot             =   Post.objects.filter(Category=category)
    context             ={}
    context['postbot']  = postbot
    context['category'] = category
    template_name       = "categoryblog.html"
    return render(request,template_name,context)

def categoryCatalog(request,slug):
    category            =    CategoryCatalog.objects.get(slug=slug)
    project             =    Project.objects.filter(category = category)
    context             =    {}
    context['project']  =    project
    context['category'] =    category
    template_name       =    'categoryportifolio.html'
    return render(request,template_name,context)
#####FIM LISTAGEM DE CATEGORIAs#####

#### Itens Individuais ####

def itenBlog(request,slug):

    post                = Post.objects.get(slug=slug)
    context             = {}
    context['post']     = post
    post.plusNumRead()
    template_name       = 'post.html'
    return render(request,template_name,context) 

def itenShop(request,slug):
    product             =  Product.objects.get(slug=slug)
    context             =  {}
    context['product']  =  product
    template_name       = 'product.html'
    return render(request,template_name,context)

def itenPortifolio(request,slug):
    project             = Project.objects.get(slug=slug)
    context             = {}
    context['project']  =   project
    template_name       = 'project.html'
    return render(request,template_name,context)
#### Fim Itens Individuais ####

#### USER ####
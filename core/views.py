# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


from .forms import Contact
from shop.models import Product,CategoryShop
from blog.models import Post,CategoryBlog
from catalog.models import Image,Project,CategoryCatalog,FavoriteProject
from django.views.decorators.csrf import csrf_exempt
#### HOME E CONTATO ####

@csrf_exempt
def favoriteProject(request):
    if request.is_ajax():
        resquest_data = request.POST
        a=list(resquest_data.items())
        project=Project.objects.get(slug=a[0][1])
        
        print(project.pk)
        favorite = FavoriteProject.objects.creat_favorite(user=request.user,project=project)
        print(favorite)
        
    return HttpResponse('OK')

def index(request):
    template_name       ='core/index.html'
    return render(request,template_name)

def contact(request):
    template_name       = 'contact.html'
    context             = {}
    if request.method=='POST':
        form = Contact(request.POST)
        if form.is_valid():
            context['is_valid']=True
            print(form.cleaned_data)
            form.sendMail(form.cleaned_data['name'],form.cleaned_data['email'],form.cleaned_data['message'],form.cleaned_data['option'])
            messages.success(request,'Menssagem Enviada!')
            #só posso usar depois do is_valid
            form= Contact()
    else:
        form                = Contact()
    context['form']     =form
    return render(request,template_name,context)
#### FIM HOME E CONTATO ####

##### LISTAGENS INDEX #####

'''
def portifolio(request):

    category            = CategoryCatalog.objects.all()
    project             = Project.objects.all()
    context             = {}

    context['project']  = project
    context['category'] = category


    template_name='portifolio.html'
    return render(request,template_name,context)




def shop(request):

    category            =CategoryShop.objects.all()
    product             =Product.objects.filter(featured=1)
    destaque            =Product.objects.filter(featured=2)


   context             ={}
    context['category'] =category
    context['product']  =product
    context['destaque'] =destaque


    template_name='product_list.html'
   return render(request,template_name,context)

def blog(request):
    
    category           = CategoryBlog.objects.all()
    postbot            = Post.objects.all()
    context={}

    context['category'] =    category
    context['postbot']  =    postbot

    template_name       = 'post_list.html'
    return render(request,template_name,context)

'''
class PortifolioListView(ListView):
    template_name       = 'portifolio.html'
    paginate_by = 4
    def get_queryset(self):
        project = Project.objects.all()
        return project
    def get_context_data(self,**kwargs):
        context = super(PortifolioListView,self).get_context_data(**kwargs)
        context['category']=CategoryCatalog.objects.all()
        return context


portifolio=PortifolioListView.as_view()

class ProductListView(ListView):
    template_name='product_list.html'
    paginate_by = 8
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


class BlogListView(ListView):
    template_name       = 'post_list.html'
    paginate_by = 5
    def get_queryset(self):
        post = Post.objects.all()
        return post
    def get_context_data(self,**kwargs):
        context = super(BlogListView,self).get_context_data(**kwargs)
        context['category']=CategoryBlog.objects.all()
        return context

blog=BlogListView.as_view()

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
    if request.user.is_authenticated:
        a = FavoriteProject.objects.filter(user=request.user,project=project).exists()
        print(a)
        context['a'] = a
    print(dir(request))
    context['project']  =   project
    template_name       = 'project.html'
    return render(request,template_name,context)
#### Fim Itens Individuais ####



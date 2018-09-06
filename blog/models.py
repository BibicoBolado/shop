# coding=utf-8
from django.db import models

# Create your models here.

class CategoryBlog(models.Model):
    name     =      models.CharField('Nome',max_length = 150)
    slug     =      models.SlugField('Atalho',max_length=100)
    description =      models.TextField('Descrição',blank=True,null=True)
    created  =      models.DateTimeField('Criado em:',auto_now_add=True)
    modified =      models.DateTimeField('Atualizado em:',auto_now=True)
    

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

class Post(models.Model):
    selection = (
        (1,'Normal'),
        (2,'Destaque'),
    )
    
    name        = models.CharField('Nome',max_length=150)
    slug        = models.SlugField('Atalho',max_length=150)
    Category    = models.ForeignKey('blog.CategoryBlog',verbose_name='Categoria',on_delete=models.CASCADE)
    about       = models.TextField('Resumo')
    text        = models.TextField('Texto. Coloca o Coração Nisso')
    created     = models.DateTimeField('Criado em:',auto_now_add=True)
    modified    = models.DateTimeField('Atualizado em:',auto_now=True)
    featured    = models.IntegerField('Destaque',choices=selection,default=1)

    imagem      = models.ImageField(
        upload_to='blog/images',verbose_name='Imagem',
        null=True,blank=True
    )

    imgfeat     = models.ImageField(
        upload_to='blog/images/destaque',verbose_name='Imagem Destaque',
        null=True,blank=True
    )
    imgcapa     = models.ImageField(
        upload_to='blog/images/destaque',verbose_name='Imagem Capa',
        null=True,blank=True
    )

    nreads       =models.IntegerField('Número Leituras',default=0)

    class Meta:
        verbose_name = 'Produtos'
        verbose_name_plural = 'Produto'
        ordering = ['name']

    def __str__(self):
        return self.name

    def plusNumRead(self):
        self.nreads+=1
        self.save()

    def timeRead(self):
        return round(len(self.text.split(" "))/133)

    def cutAbout(self):
        aux = self.about.split(" ")[:35]
        return " ".join(aux)
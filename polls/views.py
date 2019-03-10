from django.shortcuts import render, redirect

from .form import ProdutoForm
from .models import Produto

def index(request):
    data={}
    data['produtos']=Produto.objects.all()
    return render(request,'polls/index.html',data)


def createProduto(request):
    data={}

    # request.POST or None verifica se tem itens inseridos
    form=ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        # return index(request)
        # redirect altera o url
        return redirect('url_index')

    data['form']=form
    return render(request,'polls/create.html',data)


def updateProduto(request,pk):
    data={}
    produto=Produto.objects.get(pk=pk)
    form=ProdutoForm(request.POST or None,instance=produto)
    if form.is_valid():
        form.save()
        return redirect('url_index')
    data['form']=form
    return render(request,'polls/update.html',data)


def deleteProduto(request,pk):
    produto=Produto.objects.get(pk=pk)
    produto.delete()
    return redirect('url_index')


def home(request):
    data={}
    data['now'] = datetime.datetime.now()
    data['transacoes']=['t1','t2']
    return render(request,'contas/home.html',data)


def home2(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request,'contas/home.html')

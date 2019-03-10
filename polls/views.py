from django.shortcuts import render, redirect
from .form import ProdutoForm

def index(request):
    data={}
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

from django.http import HttpResponse
from django.shortcuts import render
from .forms import Form_Clientes
from .models import Clientes

def homepage(request):
    return render(request, 'clientes/home.html')

def view_clientes(request):
    #context = {}
    #context['form'] = Form_Clientes()
    #return render(request, 'clientes/clientes.html', context)
    form = Form_Clientes(request.POST)
    if form.is_valid():
        form.save()
        #return redirect(homepage)

    return render(request, 'clientes/clientes.html', {'form' : Form_Clientes})


def lista_clientes(request):
    lista_clientes = Clientes.objects.all()
    #return render(request, 'clientes/lista_clientes.html', {'lista_clientes' : lista_clientes})
    return render(request, 'clientes/lista_clientes.html', {'lista_clientes' : lista_clientes})


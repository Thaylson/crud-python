from django.shortcuts import render, redirect
from app.form import Pessoaform
from app.models import Pessoa

# Create your views here.
#home do app
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Pessoa.objects.filter(Nome__icontains=search)
    else:
        data['db'] = Pessoa.objects.all()
    
    return render(request,'index.html', data)

#pagina de fomulario
def form(request):
    data = {}
    data['form'] = Pessoaform()
    return render(request, 'form.html',data) 

#cria dado
def create(request):
    form = Pessoaform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
#visualizar os dados da tabela
def view(request,pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    return render(request,'view.html', data)  

#editar os dado
def edit(request,pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    data['form'] = Pessoaform(instance=data['db'])
    return render(request, 'form.html',data)

#atualizar os dado
def update(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    form = Pessoaform(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

#deletar dado 
def delete(request, pk):
    db = Pessoa.objects.get(pk=pk)
    db.delete()
    return redirect('home') 
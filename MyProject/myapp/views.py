from django.shortcuts import redirect, render
from myapp.models import  *
from myapp.forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'futzada/index.html',{"card": Product.objects.all()})

def create(request):
    form = ProductForm
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrado com sucesso!')
            return redirect('index')
        
    return render(request, "futzada/adicionar.html", {"forms":form})

def edit(request, id):
    produto = Product.objects.get(pk=id)
    form = ProductForm(instance=produto)
    return render(request, "futzada/update.html",{"form":form, "produto":produto})


def update(request, id):
    try:
        if request.method == "POST":
            produto = Product.objects.get(pk=id)
            form = ProductForm(request.POST, request.FILES, instance=produto)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            

def read(request, id):
    produto = Product.objects.get(pk=id)
    return render(request, "futzada/read.html", {"produto":produto})

def delete(request, id):
    produto = Product.objects.get(pk=id)
    produto.delete()
    messages.success(request, 'item foi deletado com sucesso!')
    return redirect('index')

def listar(request):
    return render(request, 'futzada/listar.html',{"cards": Product.objects.all()})

def cart(request):
    id_user = 1
    cart = Cart(id_user=id_user)
    cart.save()

def add_cart(request, id):
    id_user = 1
    cart = Cart.objects.get(id_user=id_user)
    quantity = 1
    add = CartItem(product = id, quantity = quantity, cart = cart.id)
    add.save()
    return render(request, 'futzada/cart.html',{"cards": Product.objects.all()})

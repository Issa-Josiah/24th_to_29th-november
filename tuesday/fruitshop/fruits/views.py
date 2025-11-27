from urllib import request

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import fruit
from .forms import FruitForm
from . import forms


# Create your views here.
def raw(request):
    return render(request,'fruits/raw.html')

def create (request):
    form = FruitForm()
    context = {'form': form}  # how we pass infor from view to template
    if request.method == 'POST':
        form = FruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
    return render(request, 'fruits/form.html', context)


def read_one(request, pk):
    ofu = fruit.objects.get(id = pk)
    context = {'fruit':ofu}
    return render(request, 'fruits/crefru.html', context)


def read_all(request):
    fruits = fruit.objects.all()
    context = {'fruits':fruits}
    return render(request, 'fruits/raw.html', context)

def update(request, pk):
    fruita = fruit.objects.get(id = pk)
    form = FruitForm(instance=fruita)

    if request.method == 'POST':
        form = FruitForm(request.POST , instance=fruita)
        if form.is_valid():
            form.save()
        if form.is_valid():
            form.save()
            return redirect('read')


    context = {'form': form}
    return render(request, 'fruits/form.html', context)

def delete(request, pk):
    fruita = fruit.objects.get(id=pk)
    context = {'fruit':fruita}
    if fruita:
        fruita.object.delete(id=pk)
        return redirect('read')
    return render(request, 'fruits/delete.html', context)


def prodelete(request, pk):
    fruita = fruit.objects.get(id=pk)
    context = {'fruit':fruita}
    return render(request, 'fruits/prompt_delete.html', context)
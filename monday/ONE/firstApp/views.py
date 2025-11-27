from django.shortcuts import render
from django.http import HttpResponse
from .models import Fruits
from .forms import FruitsForm

# Create your views here.
def one(request):
    return render(request, 'firstApp/main.html')

def two(request):
    fruits = Fruits.objects.all()
    # {"name" : "mango",
    #           "description" : "apple mango",
    #           "price" : 20.38}
    context = {"fruits" : fruits}

    return render(request, 'firstApp/personal.html', context)

'''
CREATE READ UPDATE DELETE CRUD OPERATIONS
'''

def createFruit(request):
    form = FruitsForm()
    context = {"form" : form}
    return render(request, 'firstApp/form.html', context )

def readAllFruits(request):
    fruits = Fruits.objects.all()
    context = {"fruits" : fruits}
    return render(request, 'firstApp/personal.html', context )

def readOneFruits(request):
    fruits = Fruits.objects.get(id=pk)
    context = {"fruits" : fruits}
    return render(request, 'firstApp/fruitdetails.html.html', context )

def update(request):
    return render(request, )

def delete(request):
    return render(request, )


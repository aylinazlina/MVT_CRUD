from django.shortcuts import render
from .models import Plants
from .forms import CreatePlantForm

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.

def plant(request):
    tree =Plants.objects.all()
    context={
        'pla':tree,
    }
    return render(request,template_name='plant.html',context=context)

def createPlant(request):
    form = CreatePlantForm()
    if request.method == 'POST':
        form =CreatePlantForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'form': form,
    }
    return render(request,template_name='create_plant.html',context=context)

def updatePlant(request,pk):
    update =Plants.objects.get(id=pk)
    form = CreatePlantForm(instance=update)
    if request.method == 'POST':
        form =CreatePlantForm(request.POST,request.FILES,instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, template_name='create_plant.html', context=context)


def deletePlants(request,pk):
    delete =Plants.objects.get(id=pk)
    if request.method == "POST":
        delete.delete()
        return redirect('/')
    context = {
        'plant': delete,
    }
    return render(request, template_name='delete.html', context=context)

from django.shortcuts import render, redirect

from .models import Squirrel
from sightings.forms import SquirrelForm

def map_of_squirrel(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
        'squirrels':squirrels,
    }
    return render(request, 'sightings/map.html', context)

def add_sightings(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sightings/')

    else:
        form = SquirrelForm()
    
    context = {
        'form': form,
    }
    return render(request, 'sightings/edit.html', context)

def update_sightings(request, squirrel_id):
    squirrel = Squirrel.objects.get(squirrel_id = squirrel_id)
    if request.method == "POST":
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}/')
    else:
        form = SquirrelForm(instance = squirrel)
    
    context = {
        'form':form,
        'squirrel':squirrel,
    }
    return render(request,'sightings/edit.html', context)

def all_sightings(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/all.html', context)

def stats(request):
    
    climbing = Squirrel.objects.filter(climbing='True').count()
    foraging = Squirrel.objects.filter(foraging='True').count()
    approaches = Squirrel.objects.filter(approaches='True').count()
    running = Squirrel.objects.filter(running='True').count()
    eating = Squirrel.objects.filter(eating='True').count()

    context ={
        'climbing':climbing,
        'foraging':foraging,
        'approaches':approaches,
        'running':running,
        'eating':eating,
    }
    return render(request, 'sightings/stats.html', context)

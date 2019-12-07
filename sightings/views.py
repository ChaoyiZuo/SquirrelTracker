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
    
    adult = Squirrel.objects.filter(age = 'adult').count()
    fur = Squirrel.objects.filter(pri_fur_color='gray').count()
    loc = Squirrel.objects.filter(location='above ground').count()
    running = Squirrel.objects.filter(running='True').count()
    eating = Squirrel.objects.filter(eating='True').count()

    context ={
        'adult':adult,
        'fur':fur,
        'loc':loc,
        'running':running,
        'eating':eating,
    }
    return render(request, 'sightings/stats.html', context)

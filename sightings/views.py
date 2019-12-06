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
    return render(request, 'sightings/add.html', {'form':form.as_p()})

def update_sightings(request, squirrel_id):
    if request.method == "POST":
        squirrel = Squirrel.objects.get(squirrel_id = squirrel_id)
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}/')
    elif request.method == 'GET':
        squirrel = Squirrel.objects.get(squirrel_id = squirrel_id)
        form = SquirrelForm(instance = squirrel)
        context = {
            'form':form.as_p(),
            'squirrel':squirrel,
        }
        return render(request,'sightings/update.html', context)

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
    return render(request, 'tracker/stats.html', context)

from django.shortcuts import render
from djangp.http import HttpResponse

from .models import Squirrel

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
    }
    return render(request, 'sightings/all.html', context)
# Create your views here.

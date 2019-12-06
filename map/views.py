from django.shortcuts import render
from sightings.models import Squirrel
import random

def map_markers(request):
    sample = random.sample(range(Squirrel.objects.count()), 50)
    squirrels = [Squirrel.objects.all()[i] for i in sample]
    context = {
            'squirrels': squirrels
            }
    return render(request, 'map/map.html', context)
    

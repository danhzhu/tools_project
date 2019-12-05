from django.shortcuts import render
from .models import Squirrel

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }
    return render(request, 'sightings/all.html', context)

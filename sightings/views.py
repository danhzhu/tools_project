from django.shortcuts import render
from .models import Squirrel
from django.shortcuts import redirect
from .forms import SquirrelForm

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }
    return render(request, 'sightings/all.html', context)

def edit_squirrels(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id = unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        form = SquirrelForm(instance = squirrel)
    context = {
            'form': form,
            }
    return render(request, 'sightings/edit_add.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm()
        
    context = {
            'form': form,
            'jazz': True,
            }
    return render(request, 'sightings/edit_add.html', context)

def stats(request):
    total = Squirrel.objects.count()
    adult = Squirrel.objects.filter(age = 'Adult').count()
    juvenile = Squirrel.objects.filter(age = 'Juvenile').count()
    gray = Squirrel.objects.filter(primary_fur_color = 'Gray').count()
    cinnamon = Squirrel.objects.filter(primary_fur_color = 'Cinnamon').count()
    black = Squirrel.objects.filter(primary_fur_color = 'Black').count()
    above = Squirrel.objects.filter(location = 'Above Ground').count()
    ground = Squirrel.objects.filter(location = 'Ground Plane').count()
    running = Squirrel.objects.filter(running = True).count()
    climbing = Squirrel.objects.filter(climbing = True).count()
    moans = Squirrel.objects.filter(moans = True).count()

    context = {
                'total': total,
                'adult': adult,
                'juvenile': juvenile,
                'gray': gray,
                'cinnamon': cinnamon,
                'black': black,
                'above': above,
                'ground': ground,
                'running': running,
                'climbing': climbing,
                'moans': moans,
                }

    return render(request, 'sightings/stats.html', context)


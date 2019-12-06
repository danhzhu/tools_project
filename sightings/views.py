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
            'form' : form,
            }
    return render(request, 'sightings/edit_add.html', context)

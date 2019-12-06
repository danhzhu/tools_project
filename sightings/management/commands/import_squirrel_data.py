from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
import os
from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Import csv into database'

    def add_arguments(self, parser):
         parser.add_argument('path', type = str, help = 'Get the file path')

    def handle(self, *args, **options):
        path = options['path']
        if not os.path.exists(path):
            raise CommandError(f'Path:{path}does not exist.')

        with open(options['path']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
            
            for item in data:
                latitude = item['Y']
                longitude = item['X']
                unique_squirrel_id = item['Unique Squirrel ID']

                if (item['Shift'].lower() in ['am', 'pm']):
                    shift = item['Shift'].lower()
                else:
                    shift = ''
    
                date = item['Date']

                if (item['Age'].lower() in ['adult', 'juvenile']):
                    age = item['Age'].lower()
                else:
                    age = ''

                if (item['Primary Fur Color'].lower() in ['black', 'gray', 'cinnamon']):
                    primary_fur_color = item['Primary Fur Color'].lower()
                else:
                    primary_fur_color = ''

                if (item['Location'].lower() in ['ground plane', 'above ground']):
                    location = item['Location'].lower()
                else:
                    location = ''

                specific_location = item['Specific Location']

                running = True if "true" in item['Running'].lower() else False
                chasing = True if "true" in item['Chasing'].lower() else False
                climbing = True if "true" in item['Climbing'].lower() else False
                eating = True if "true" in item['Eating'].lower() else False
                foraging = True if "true" in item['Foraging'].lower() else False

                other_activities = item['Other Activities']

                kuks = True if "true" in item['Kuks'].lower() else False
                quaas = True if "true" in item['Quaas'].lower() else False
                moans = True if "true" in item['Moans'].lower() else False
                tail_flags = True if "true" in item['Tail flags'].lower() else False
                tail_twitches = True if "true" in item['Tail twitches'].lower() else False
                approaches = True if "true" in item['Approaches'].lower() else False
                indifferent = True if "true" in item['Indifferent'].lower() else False
                runs_from = True if "true" in item['Runs from'].lower() else False
    
                squirrel = Squirrel(
                    latitude = latitude,
                    longitude = longitude,
                    unique_squirrel_id = unique_squirrel_id,
                    shift = shift,
                    date = date,
                    age = age,
                    primary_fur_color = primary_fur_color,
                    location = location,
                    specific_location = specific_location,
                    running = running,
                    chasing = chasing,
                    climbing = climbing,
                    eating = eating,
                    foraging = foraging,
                    other_activities = other_activities,
                    kuks = kuks,
                    quaas = quaas,
                    moans = moans,
                    tail_flags = tail_flags,
                    tail_twitches = tail_twitches,
                    approaches = approaches,
                    indifferent = indifferent,
                    runs_from = runs_from,
                )
                squirrel.save()


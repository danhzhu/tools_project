from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'Export from db into csv'

    def add_arguments(self, parser):
        parser.add_argument('path', help = 'Get the file path')

    def handle(self, *args, **options):
        path = options['path']
        csvfile = open(path, 'w')
        writer = csv.writer(csvfile)
        writer.writerow(['Index', 'Longitude','Latitude', 'Unique Squirrel ID',
            'Shift', 'Date','Age', 'Primary Fur Color', 'Location',
            'Specific Location', 'Running', 'Chasing', 'Climbing', 
            'Eating', 'Foraging','Other Activities', 'Kuks', 'Quaas',
            'Moans', 'Tail flags','Tail twitches', 'Approaches',
            'Indifferernt', 'Runs from'])
        for obj in Squirrel.objects.all():
            row = []
            for field in Squirrel._meta.fields:
                row.append(getattr(obj, field.name))
            writer.writerow(row)
        csvfile.close()

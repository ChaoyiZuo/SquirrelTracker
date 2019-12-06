import csv
import datetime
from django.core.management.base import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Imports data from 2018 Central Park Squirrel Census data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='file path of csv data')

    def handle(self, *args, **options):
        with open(options['path']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            for i in ('Running','Chasing','Climbing','Eating','Foraging','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from'):
                if item[i] == 'false':
                    item[i] = False
                else:
                    item[i] = True
            squirrel = Squirrel(
                lon = item['X'],
                lat = item['Y'],
                squirrel_id = item['Unique Squirrel ID'],
                shift = item['Shift'],
                date = datetime.datetime.strptime(item['Date'].strip(),'%m%d%Y').date(),
                age = item['Age'],
                pri_fur_color = item['Primary Fur Color'],
                location = item['Location'],
                specific_location = item['Specific location'],
                running = item['Running'],
                chasing = item['Chasing'],
                climbing = item['Climbing'],
                eating = item['Eating'],
                foraging = item['Foraging'],
                other_activities = item['Other Activities'],
                kuks = item['Kuks'],
                quaas = item['Quaas'],
                moans = item['Moans'],
                tail_flags = item['Tail flags'],
                tail_twitches = item['Tail twitches'],
                approaches = item['Approaches'],
                indifferent = item['Indifferent'],
                runs_from = item['Runs from'],       
            )

            squirrel.save()


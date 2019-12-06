import csv
from django.core.management.base import BaseCommand,CommandError
from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Export data in csv format'

    def add_arguments(self,parser):
        parser.add_argument('path', type=str, help='path of csv file')

    def handle(self,*args,**options):
        with open(options['path'],mode='w') as fp:
            writer = csv.writer(fp,delimiter=',')
            all_fields = [f.name for f in Squirrel._meta.get_fields()]
            fieldnames = [Squirrel._meta.get_field(i).help_text for i in all_fields[1:]]
            writer.writerow(fieldnames)
            for j in range(len(Squirrel.objects.all())):
                row = list()
                for i in all_fields:
                    if i == 'id': continue
                    row.append(getattr(Squirrel.objects.all()[j],i))
                writer.writerow(row)
        fp.close



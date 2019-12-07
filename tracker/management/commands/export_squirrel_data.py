from django.core.management.base import BaseCommand, CommandError
from tracker.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
        

    def handle(self, *args, **options):
        path = options['path']
        with open(path,'w',newline='') as f:
            model = Squirrel
            field = [_.name for _ in model._meta.fields]
            writer = csv.writer(f,quoting=csv.QUOTE_ALL)
            writer.writerow(field)
            for item in model.objects.all():
                writer.writerow([getattr(item,ins) for ins in field])

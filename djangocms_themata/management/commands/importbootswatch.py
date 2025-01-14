from django.core.management.base import BaseCommand, CommandError

from djangocms_themata.util import load_stylesheets

class Command(BaseCommand):
    help = 'Imports the Bootswatch stylesheets.'

    def handle(self, *args, **options):
        load_stylesheets()
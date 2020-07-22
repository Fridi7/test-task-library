from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'rolls migrations and fixtures'

    def handle(self, *args, **options):
        call_command("makemigrations", interactive=False)
        call_command("migrate", interactive=False)
        call_command("loaddata", "fixtures/fixtures.json")

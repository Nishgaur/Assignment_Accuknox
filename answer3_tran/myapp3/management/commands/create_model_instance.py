from django.core.management.base import BaseCommand
from myapp3.models import create_model_instance

class Command(BaseCommand):
    help = 'Creates a model instance and applies the signal logic'

    def handle(self, *args, **kwargs):
        create_model_instance()
        self.stdout.write(self.style.SUCCESS('Successfully created model instance'))

from django.core.management.base import BaseCommand
from users.models import User
from django_seed import Seed


class Command(BaseCommand):

    def add_arguments(self, parse):
        parse.add_argument('--number', default=1, help="How many users you want to create")

    def handle(self, *args, **options):
        number = int(options.get('number'))
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    def handle(self, *args, **options):

        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for fac in facilities:

            Facility.objects.create(name=fac)
        
        self.stdout.write(self.style.SUCCESS(f'{len(facilities)} facilities created!'))
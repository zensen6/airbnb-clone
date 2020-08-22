import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates rooms"
    
    def add_arguments(self, parser):

        parser.add_argument(
            '--number', 
            default=2, 
            help="how many rooms you want to add"
        )

    def handle(self, *args, **option):

        number = int(option.get('number'))
        host = user_models.User.objects.all()
        room_type = room_models.RoomType.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(host),
                "room_type": lambda x: random.choice(room_type),
                "guests": lambda x: random.randint(1, 300), 
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            }
           
        )
        rooms_id = seeder.execute()
        rooms_id = flatten(rooms_id.values())
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in rooms_id:
            R = room_models.Room.objects.get(pk=pk)
            
            for number_photo in range(3, random.randint(10, 30)):   

                room_models.Photo.objects.create(   
                    caption=seeder.faker.sentence(),  
                    room=R,
                    file=f"room_photos/{random.randint(1,31)}.webp"
                )

            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    R.amenities.add(a)

            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    R.facilities.add(f)

            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    R.house_rules.add(r)       
    
        self.stdout.write(self.style.SUCCESS(f"{number} room created"))
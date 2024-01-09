from django.core.management import BaseCommand

from myapp.models import Car


class Command(BaseCommand):
    def handle(self, *args, **options):
        name_cars = [
            "Mercedes",
            "BMW",
            "Audi",
            "Tracker",
            "Spark"
        ]

        for cars in name_cars:
            car, created = Car.objects.get_or_create(name=cars)
            self.stdout.write(f"Created car {car.name}")
        self.stdout.write(self.style.SUCCESS("Created cars!"))
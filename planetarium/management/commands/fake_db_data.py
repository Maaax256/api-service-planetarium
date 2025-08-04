from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from planetarium.models import ShowTheme, AstronomyShow, PlanetariumDome, ShowSession
import random

class Command(BaseCommand):
    help = "Generate fake data for the database"
    objects_number = 10

    @transaction.atomic
    def handle(self, *args, **kwargs):
        fake = Faker()

        show_themes = []
        for _ in range(self.objects_number):
            theme = ShowTheme.objects.create(name=fake.unique.word())
            show_themes.append(theme)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {self.objects_number} ShowTheme instances"
            )
        )

        astronomy_shows = []
        for _ in range(self.objects_number):
            show = AstronomyShow.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.text()
            )
            show.show_themes.set(
                random.sample(
                    show_themes,
                    k=random.randint(1, len(show_themes))
                )
            )
            astronomy_shows.append(show)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {self.objects_number} AstronomyShow instances"
            )
        )

        planetarium_domes = []
        for _ in range(self.objects_number):
            dome = PlanetariumDome.objects.create(
                name=fake.unique.word(),
                rows=random.randint(5, 10),
                seats_in_row=random.randint(10, 20)
            )
            planetarium_domes.append(dome)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {self.objects_number} PlanetariumDome instances"
            )
        )

        show_sessions = []
        while len(show_sessions) != self.objects_number:
            astronomy_show = random.choice(astronomy_shows)
            planetarium_dome = random.choice(planetarium_domes)
            show_time = fake.date_time_between(start_date="now", end_date="+30d")
            session = ShowSession.objects.create(
                astronomy_show=astronomy_show,
                planetarium_dome=planetarium_dome,
                show_time=show_time
            )
            show_sessions.append(session)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {self.objects_number} ShowSession instances"
            )
        )

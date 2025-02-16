import random
from django.core.management.base import BaseCommand
from faker import Faker
from crime_api.models import CrimeReport, Upvote

class Command(BaseCommand):
    help = 'Generate fake upvote data for testing'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Get all CrimeReport IDs
        crime_report_ids = list(CrimeReport.objects.values_list('_id', flat=True))

        if not crime_report_ids:
            self.stdout.write(self.style.ERROR('No CrimeReport records found. Please populate the database first.'))
            return

        # Generate 330099 fake upvotes
        for _ in range(330099):
            # Get a random CrimeReport ID
            random_id = random.choice(crime_report_ids)
            crime_report = CrimeReport.objects.get(_id=random_id)

            # Create an Upvote
            Upvote.objects.create(
                crime_report=crime_report,
                officer_name=fake.name(),
                officer_email=fake.email(),
                badge_number=fake.random_number(digits=5)
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated 330099 upvotes'))

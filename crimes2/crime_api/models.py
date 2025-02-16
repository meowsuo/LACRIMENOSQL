import random
from django.core.management.base import BaseCommand
from faker import Faker
from crime_api.models import CrimeReport, Upvote

class Command(BaseCommand):
    help = 'Generate fake upvote data for testing'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Get all CrimeReport IDs
        crime_report_ids = list(CrimeReport.objects.values_list('dr_no', flat=True))

        if not crime_report_ids:
            self.stdout.write(self.style.ERROR('No CrimeReport records found. Please populate the database first.'))
            return

        # Generate 1000 fake upvotes
        for _ in range(330099):
            # Get a random CrimeReport ID
            random_id = random.choice(crime_report_ids)

            try:
                # Try to get the CrimeReport
                crime_report = CrimeReport.objects.get(dr_no=random_id)
            except CrimeReport.DoesNotExist:
                # If the CrimeReport does not exist, skip this iteration
                self.stdout.write(self.style.WARNING(f'CrimeReport with dr_no={random_id} does not exist. Skipping.'))
                continue

            # Create an Upvote
            Upvote.objects.create(
                crime_report=crime_report,
                officer_name=fake.name(),
                officer_email=fake.email(),
                badge_number=fake.random_number(digits=5)
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated upvotes'))
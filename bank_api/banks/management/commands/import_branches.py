
import csv
from django.core.management.base import BaseCommand
from banks.models import Bank, Branch

class Command(BaseCommand):
    help = 'Import bank branches from CSV'

    def handle(self, *args, **kwargs):
        with open('F:\Assignment/bank_branches.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bank, created = Bank.objects.get_or_create(
                    name=row['bank_name'],
                    bank_id=row['bank_id']
                )
                Branch.objects.create(
                    ifsc=row['ifsc'],
                    branch=row['branch'],
                    address=row['address'],
                    city=row['city'],
                    district=row['district'],
                    state=row['state'],
                    bank=bank
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported branch data'))

import requests

from django.core.management.base import BaseCommand, CommandError

from bs4 import BeautifulSoup

from tax_rates.models import TaxUnitValue



class Command(BaseCommand):
    help = ('Command to import the tax unit value needed to calculate the taxes'
            'to be paid at the end of the year')

    def add_arguments(self, parser):
        """"""
        # parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        """
        Function that handles the command line interface, try except is
        not recommended as it is too wide, but in this case it is needed
        for the command to gather the values without failure.
        """
        r = requests.get('https://www.sunat.gob.pe/indicestasas/uit.html')
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table', class_='tb02')
        table_body = table.find('tbody')
        for row in table_body.find_all('tr')[1:]:
            try:
                column = row.find_all('td')
                year = column[0].find('p').getText()
                value = column[1].find('p').getText()

                tax_unit_value, created = TaxUnitValue.objects.update_or_create(
                    year=clean_year(year),
                    defaults={'value': clean_value(value)}
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully {'created' if created else 'updated'} for"
                        f" {year}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Error for {column.beutify}: {e}")
                )
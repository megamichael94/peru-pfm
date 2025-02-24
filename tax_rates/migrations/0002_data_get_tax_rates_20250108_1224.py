import requests

from django.db import migrations
from bs4 import BeautifulSoup
from tax_rates.models import TaxUnitValue


def clean_year(year):
    if '1993' not in year:
        return int(year)
    return 1993

def clean_value(value):
    return ''.join(char for char in value if char.isdigit())


def get_tax_rates(apps, schema_editor):

    TaxUnitValue = apps.get_model('tax_rates', 'TaxUnitValue')
    r = requests.get('https://www.sunat.gob.pe/indicestasas/uit.html')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', class_='tb02')
    table_body = table.find('tbody')
    for row in table_body.find_all('tr')[1:]:

        column = row.find_all('td')
        year = column[0].find('p').getText()
        value = column[1].find('p').getText()

        tax_unit_value, _ = TaxUnitValue.objects.update_or_create(
            year=clean_year(year),
            defaults={'value': clean_value(value)}
        )

def reverse_get_tax_rates(apps, schema_editor):
    TaxUnitValue = apps.get_model('tax_rates', 'TaxUnitValue')


class Migration(migrations.Migration):

    dependencies = [
        ('tax_rates', '0001_initial'),
    ]

    operations = [
    ]

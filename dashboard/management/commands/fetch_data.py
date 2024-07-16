from django.core.management.base import BaseCommand
from dashboard.models import Country, DebtEducationData
import requests


class Command(BaseCommand):
    help = 'Fetch data for the dashboard'

    def handle(self, *args, **kwargs):
        # Clear existing data
        DebtEducationData.objects.all().delete()
        Country.objects.all().delete()

        def fetch_country_data(country_code, country_name):
            # Fetch external debt data
            debt_response = requests.get(
                f'https://api.worldbank.org/v2/country/{country_code}/indicator/DT.DOD.DLXF.CD?date=2010:2020&format=json')
            debt_data = debt_response.json()
            print(f'Debt data for {country_name}: {debt_data}')

            # Fetch education expenditure data
            education_response = requests.get(
                f'https://api.worldbank.org/v2/country/{country_code}/indicator/SE.XPD.TOTL.GB.ZS?date=2010:2020&format=json')
            education_data = education_response.json()
            print(f'Education data for {country_name}: {education_data}')

            country, created = Country.objects.get_or_create(name=country_name)

            for debt_entry, education_entry in zip(debt_data[1], education_data[1]):
                external_debt = debt_entry['value']
                education_expenditure = education_entry['value']

                if education_expenditure is not None:
                    DebtEducationData.objects.create(
                        country=country,
                        year=debt_entry['date'],
                        external_debt=external_debt,
                        education_expenditure=education_expenditure
                    )
                else:
                    self.stdout.write(self.style.WARNING(
                        f"Skipping entry for {country_name} in {debt_entry['date']}: education expenditure is None"))

        countries = {
            'ETH': 'Ethiopia',
            'BWA': 'Botswana',
            # 'CHN': 'China',
            'ZAF': 'South Africa',
            'TZA': 'Tanzania',
            'AGO': 'Angola'
        }

        for code, name in countries.items():
            fetch_country_data(code, name)

        self.stdout.write(self.style.SUCCESS('Successfully fetched data'))

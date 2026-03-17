from django.core.management.base import BaseCommand
from main.models import House


class Command(BaseCommand):
    help = 'Populate database with sample house data'

    def handle(self, *args, **options):
        # Sample house data
        sample_houses = [
            {
                'address': '123 Main Street',
                'city': 'Amsterdam',
                'province': 'Noord-Holland',
                'price': '€450,000',
                'bedrooms': 3,
                'bathrooms': 2,
                'area': '120 m²',
            },
            {
                'address': '456 Canal Road',
                'city': 'Utrecht',
                'province': 'Utrecht',
                'price': '€380,000',
                'bedrooms': 2,
                'bathrooms': 1,
                'area': '95 m²',
            },
            {
                'address': '789 Park Lane',
                'city': 'Rotterdam',
                'province': 'Zuid-Holland',
                'price': '€420,000',
                'bedrooms': 4,
                'bathrooms': 2,
                'area': '140 m²',
            },
            {
                'address': '321 Garden Way',
                'city': 'The Hague',
                'province': 'Zuid-Holland',
                'price': '€520,000',
                'bedrooms': 3,
                'bathrooms': 2,
                'area': '135 m²',
            },
            {
                'address': '654 River View',
                'city': 'Eindhoven',
                'province': 'Noord-Brabant',
                'price': '€350,000',
                'bedrooms': 2,
                'bathrooms': 1,
                'area': '85 m²',
            },
            {
                'address': '987 Street Square',
                'city': 'Groningen',
                'province': 'Groningen',
                'price': '€290,000',
                'bedrooms': 2,
                'bathrooms': 1,
                'area': '80 m²',
            },
            {
                'address': '135 Sunset Boulevard',
                'city': 'Arnhem',
                'province': 'Gelderland',
                'price': '€310,000',
                'bedrooms': 3,
                'bathrooms': 2,
                'area': '110 m²',
            },
            {
                'address': '246 Meadow Drive',
                'city': 'Breda',
                'province': 'Noord-Brabant',
                'price': '€395,000',
                'bedrooms': 3,
                'bathrooms': 2,
                'area': '125 m²',
            },
            {
                'address': '369 Forest Path',
                'city': 'Maastricht',
                'province': 'Limburg',
                'price': '€340,000',
                'bedrooms': 2,
                'bathrooms': 1,
                'area': '100 m²',
            },
            {
                'address': '789 Harbor Point',
                'city': 'Zwolle',
                'province': 'Overijssel',
                'price': '€325,000',
                'bedrooms': 2,
                'bathrooms': 1,
                'area': '90 m²',
            },
        ]

        # Clear existing houses
        House.objects.all().delete()

        # Create houses
        for house_data in sample_houses:
            House.objects.create(**house_data)
            self.stdout.write(self.style.SUCCESS(f"Created house: {house_data['address']}"))

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample houses'))

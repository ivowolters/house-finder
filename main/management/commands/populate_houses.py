from django.core.management.base import BaseCommand
from django.conf import settings
from main.models import House
from main.blob_storage import upload_blob


class Command(BaseCommand):
    help = 'Populate database with sample house data and upload to blob storage'

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
        
        # Upload database to blob storage
        db_path = settings.DATABASES['default']['NAME']
        self.stdout.write('Uploading database to blob storage...')
        
        try:
            blob_path = upload_blob(db_path, blob_name='db.sqlite3', container_name='houses')
            if blob_path:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully uploaded database to {blob_path}')
                )
            else:
                self.stdout.write(self.style.WARNING('Failed to upload database to blob storage'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Error uploading to blob storage: {str(e)}'))

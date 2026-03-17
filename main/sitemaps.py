from django.contrib.sitemaps import Sitemap
from django.urls import reverse
import csv
import os


class StaticSitemap(Sitemap):
    """Sitemap for static pages"""
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return ['home', 'houses', 'about']

    def location(self, item):
        return reverse(item)


class CitiesSitemap(Sitemap):
    """Sitemap for all cities from CSV"""
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        csv_path = os.path.join(os.path.dirname(__file__), 'data', 'cities.csv')
        cities = []
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    cities.append(row['city_name'])
        except FileNotFoundError:
            cities = []
        
        return cities

    def location(self, item):
        # Convert city name to URL slug (e.g., "The Hague" -> "the-hague")
        slug = item.lower().replace(' ', '-')
        return f'/{slug}/'


class HousesSitemap(Sitemap):
    """Sitemap for houses in sample data"""
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        # Get unique cities from the sample houses
        cities = [
            'Amsterdam', 'Utrecht', 'Rotterdam', 'The Hague',
            'Eindhoven', 'Groningen', 'Arnhem', 'Breda',
            'Maastricht', 'Zwolle'
        ]
        return cities

    def location(self, item):
        # Convert city name to URL slug
        slug = item.lower().replace(' ', '-')
        return f'/{slug}/'


sitemaps = {
    'static': StaticSitemap,
    'cities': CitiesSitemap,
    'houses': HousesSitemap,
}

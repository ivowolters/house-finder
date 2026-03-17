from django.shortcuts import render
from django.http import HttpResponse
import csv
import os
import json

# Create your views here.

def home(request):
    # Load city data from CSV
    csv_path = os.path.join(os.path.dirname(__file__), 'data', 'cities.csv')
    city_data = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                city_data.append({
                    'city': row['city_name'],
                    'province': row['province'],
                    'population': int(row['population']) if row['population'].isdigit() else 0,
                    'postal_prefix': row['postal_code_prefix']
                })
    except FileNotFoundError:
        # Fallback to empty list if CSV not found
        city_data = []
    
    # Convert to JSON for JavaScript
    city_data_json = json.dumps(city_data)
    
    context = {
        'city_data_json': city_data_json
    }
    
    return render(request, 'main/home.html', context)

def houses(request):
    # Static list of 10 sample houses
    houses_list = [
        {
            'id': 1,
            'address': '123 Main Street',
            'city': 'Amsterdam',
            'province': 'Noord-Holland',
            'price': '€450,000',
            'bedrooms': 3,
            'bathrooms': 2,
            'area': '120 m²',
            'image': '🏠'
        },
        {
            'id': 2,
            'address': '456 Canal Road',
            'city': 'Utrecht',
            'province': 'Utrecht',
            'price': '€380,000',
            'bedrooms': 2,
            'bathrooms': 1,
            'area': '95 m²',
            'image': '🏠'
        },
        {
            'id': 3,
            'address': '789 Park Lane',
            'city': 'Rotterdam',
            'province': 'Zuid-Holland',
            'price': '€420,000',
            'bedrooms': 4,
            'bathrooms': 2,
            'area': '140 m²',
            'image': '🏠'
        },
        {
            'id': 4,
            'address': '321 Garden Way',
            'city': 'The Hague',
            'province': 'Zuid-Holland',
            'price': '€520,000',
            'bedrooms': 3,
            'bathrooms': 2,
            'area': '135 m²',
            'image': '🏠'
        },
        {
            'id': 5,
            'address': '654 River View',
            'city': 'Eindhoven',
            'province': 'Noord-Brabant',
            'price': '€350,000',
            'bedrooms': 2,
            'bathrooms': 1,
            'area': '85 m²',
            'image': '🏠'
        },
        {
            'id': 6,
            'address': '987 Street Square',
            'city': 'Groningen',
            'province': 'Groningen',
            'price': '€290,000',
            'bedrooms': 2,
            'bathrooms': 1,
            'area': '80 m²',
            'image': '🏠'
        },
        {
            'id': 7,
            'address': '135 Sunset Boulevard',
            'city': 'Arnhem',
            'province': 'Gelderland',
            'price': '€310,000',
            'bedrooms': 3,
            'bathrooms': 2,
            'area': '110 m²',
            'image': '🏠'
        },
        {
            'id': 8,
            'address': '246 Meadow Drive',
            'city': 'Breda',
            'province': 'Noord-Brabant',
            'price': '€395,000',
            'bedrooms': 3,
            'bathrooms': 2,
            'area': '125 m²',
            'image': '🏠'
        },
        {
            'id': 9,
            'address': '369 Forest Path',
            'city': 'Maastricht',
            'province': 'Limburg',
            'price': '€340,000',
            'bedrooms': 2,
            'bathrooms': 1,
            'area': '100 m²',
            'image': '🏠'
        },
        {
            'id': 10,
            'address': '789 Harbor Point',
            'city': 'Zwolle',
            'province': 'Overijssel',
            'price': '€325,000',
            'bedrooms': 2,
            'bathrooms': 1,
            'area': '90 m²',
            'image': '🏠'
        },
    ]
    
    # Get search parameters from GET request
    cities = request.GET.get('cities', '').split(',') if request.GET.get('cities') else []
    provinces = request.GET.get('provinces', '').split(',') if request.GET.get('provinces') else []
    
    # Clean up empty strings
    cities = [c.strip() for c in cities if c.strip()]
    provinces = [p.strip() for p in provinces if p.strip()]
    
    # Filter houses based on search parameters (if any provided)
    if cities or provinces:
        filtered_houses = []
        for house in houses_list:
            if (not cities and not provinces) or \
               (house['city'] in cities) or \
               (house['province'] in provinces):
                filtered_houses.append(house)
        houses_list = filtered_houses
    
    context = {
        'houses': houses_list,
        'search_cities': cities,
        'search_provinces': provinces,
        'total_results': len(houses_list)
    }
    
    return render(request, 'main/houses.html', context)

def about(request):
    return HttpResponse('<h1>About Page</h1><p>This is a Django website for house finding!</p>')


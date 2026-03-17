from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
import csv
import os
import json
from .models import House

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

def houses(request, city=None):
    # Get search parameters from GET request
    cities = request.GET.get('cities', '').split(',') if request.GET.get('cities') else []
    provinces = request.GET.get('provinces', '').split(',') if request.GET.get('provinces') else []
    
    # Clean up empty strings
    cities = [c.strip() for c in cities if c.strip()]
    provinces = [p.strip() for p in provinces if p.strip()]
    
    # If city is provided in URL (catch-all), use it as a search filter
    # Convert hyphens to spaces to match city names (e.g., "the-hague" -> "The Hague")
    if city and not cities and not provinces:
        # Capitalize the city name properly
        url_city = city.replace('-', ' ').title()
        cities = [url_city]
    
    # Build query filter
    query = Q()
    
    if cities:
        # Filter by cities (case-insensitive)
        city_filter = Q()
        for c in cities:
            city_filter |= Q(city__iexact=c)
        query &= city_filter
    
    if provinces:
        # Filter by provinces (case-insensitive)
        province_filter = Q()
        for p in provinces:
            province_filter |= Q(province__iexact=p)
        query &= province_filter
    
    # Query database, filter available houses
    if query:
        houses_list = House.objects.filter(query, available=True)
    else:
        houses_list = House.objects.filter(available=True)
    
    # Convert houses to list format for template (include emoji icon)
    houses_data = []
    for house in houses_list:
        houses_data.append({
            'id': house.id,
            'address': house.address,
            'city': house.city,
            'province': house.province,
            'price': house.price,
            'bedrooms': house.bedrooms,
            'bathrooms': house.bathrooms,
            'area': house.area,
            'image': '🏠'
        })
    
    context = {
        'houses': houses_data,
        'search_cities': cities,
        'search_provinces': provinces,
        'total_results': len(houses_data)
    }
    
    return render(request, 'main/houses.html', context)

def about(request):
    return HttpResponse('<h1>About Page</h1><p>This is a Django website for house finding!</p>')

def robots_txt(request):
    """Serve robots.txt with sitemap location"""
    robots_content = """User-agent: *
Allow: /
Sitemap: http://example.com/sitemap.xml
"""
    return HttpResponse(robots_content, content_type='text/plain')

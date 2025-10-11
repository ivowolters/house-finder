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

def about(request):
    return HttpResponse('<h1>About Page</h1><p>This is a Django website for house finding!</p>')

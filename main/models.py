from django.db import models

# Create your models here.

class House(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('condo', 'Condominium'),
        ('townhouse', 'Townhouse'),
        ('villa', 'Villa'),
    ]
    
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.CharField(max_length=50)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, default='house')
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.address} - {self.city}"
    
    class Meta:
        ordering = ['-created_at']

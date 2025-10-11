from django.contrib import admin
from .models import House

# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'property_type', 'bedrooms', 'bathrooms', 'city', 'available', 'created_at')
    list_filter = ('property_type', 'available', 'city', 'state')
    search_fields = ('title', 'address', 'city', 'description')
    list_editable = ('available',)
    ordering = ('-created_at',)

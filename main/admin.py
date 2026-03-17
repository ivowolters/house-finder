from django.contrib import admin
from .models import House

# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'price', 'bedrooms', 'bathrooms', 'province', 'available', 'created_at')
    list_filter = ('property_type', 'available', 'city', 'province')
    search_fields = ('address', 'city', 'province', 'description')
    list_editable = ('available',)
    ordering = ('-created_at',)

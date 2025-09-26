from django.contrib import admin
from .models import Pet, Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'price', 'is_available', 'category']
    list_filter = ['species', 'category', 'is_available']
    search_fields = ['name', 'breed', 'description']
    list_editable = ['price', 'is_available']
    
    # Make image upload more user-friendly
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'species', 'breed', 'category')
        }),
        ('Details', {
            'fields': ('color', 'description', 'price', 'is_available')
        }),
        ('Image', {
            'fields': ('image',),
            'description': 'Upload a pet image (JPG, PNG, GIF, or WebP)'
        }),
    )
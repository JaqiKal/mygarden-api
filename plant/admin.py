from django.contrib import admin
from .models import PlantVariety

# Register your models here.
@admin.register(PlantVariety)
class PlantVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'latin_name', 'purchase_date', 'purchased_from',)
    search_fields = ('name', 'category', 'latin_name',)
    list_filter = ('category', 'purchase_date',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

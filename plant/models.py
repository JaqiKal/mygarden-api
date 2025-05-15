# plant model 
from django.db import models

# Create your models here.
class PlantVariety(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # e.g. vegetable, herb, tree
    latin_name = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    purchased_from = models.CharField(max_length=150, blank=True)
    seed_date = models.DateField(null=True, blank=True)
    transplant_date = models.DateField(null=True, blank=True)
    purchase_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    initial_quantity = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

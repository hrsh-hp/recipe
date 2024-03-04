from django.contrib import admin
from .models import Recipe, Ingredients
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredients)
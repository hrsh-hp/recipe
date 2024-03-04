from django.contrib import admin
from .models import CustomUser, LikedRecipe
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(LikedRecipe)
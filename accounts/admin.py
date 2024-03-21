from django.contrib import admin
from .models import CustomUser, LikedRecipe, menu, Blog
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(LikedRecipe)
admin.site.register(menu)
admin.site.register(Blog)
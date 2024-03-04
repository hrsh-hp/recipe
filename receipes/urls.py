from django.urls import path
from .views import add_recipe,get_recipe

app_name = 'receipes'

urlpatterns = [
    path('add-recipe/',add_recipe,name='add_recipe'),
    path('<slug>',get_recipe,name="get_recipe"),
]
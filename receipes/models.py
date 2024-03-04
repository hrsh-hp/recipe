from django.db import models
from django.utils.text import slugify
from helpers import generate_unique_hash

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField( max_length=150)
    description = models.TextField()
    image = models.ImageField( upload_to="recipe/images/", null=True, blank=True)
    video = models.FileField( upload_to="recipe/videos/",null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    preparation_time = models.IntegerField(null=True,blank=True,default=0)
    slug = models.SlugField(unique=True,null=True, blank=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.recipe_name) +"-"+ generate_unique_hash()
        super(Recipe, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.recipe_name
    
    def get_total_ingredients(self):
        ingredients = Ingredients.objects.all().count()
        return ingredients

class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredient", on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=100)
    amount = models.CharField(max_length=150, null=True,blank=True)
    
    def __str__(self):
        return self.ingredient_name + " - " + self.recipe.recipe_name
    
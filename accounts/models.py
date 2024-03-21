from email import message
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from django.core.validators import MaxValueValidator,MinValueValidator
from helpers import generate_unique_hash
from receipes.models import Recipe

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='username',null=True, blank=True)
    email = models.EmailField(unique=True,max_length = 255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    user_image = models.ImageField(upload_to = 'images/user/',null=True, blank=True)
    phone_no = models.IntegerField(validators=[MaxValueValidator(999999999999),MinValueValidator(000000000000)],null=True, blank=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    temp_email = models.EmailField(null=True,blank=True,max_length = 255,default= None)
    forgot_password_token = models.SlugField(unique=True, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def name(self):
        return self.first_name +" "+ self.last_name
    
    def __str__(self) -> str:
        return self.email
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_hash()
        super(CustomUser, self).save(*args, **kwargs)
        
        
class LikedRecipe(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="liked_recipes")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True,blank=True, related_name="liked_by")
    
    
    def __str__(self):
        return self.user.email + " liked " + self.recipe.recipe_name


    
class menu(models.Model):
    DAYS = [
    ("monday","Monday"),
    ("tuesday","Tuesday"),
    ("wednesday","Wednesday"),
    ("tursday","Trusday"),
    ("friday","Friday"),
    ("saturday","Saturday"),
    ("sunday","Sunday"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="menu")
    day = models.CharField( max_length=50,choices= DAYS)
    breakfast = models.ForeignKey("receipes.Recipe", related_name='break_fast', on_delete=models.CASCADE)
    lunch = models.ForeignKey("receipes.Recipe", related_name='lunch', on_delete=models.CASCADE)
    dinner = models.ForeignKey("receipes.Recipe", related_name='dinner', on_delete=models.CASCADE)
    updated_at = models.DateField(auto_now=True)    
    

    def __str__(self) -> str:
        return self.user.email+ " - " + self.day
    
class Blog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="blog")
    title = models.CharField( max_length=50)
    category = models.CharField( max_length=50)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_hash()
        super(Blog, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.title
    
    
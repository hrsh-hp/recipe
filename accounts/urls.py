from django.urls import path
from .views import LoginView,Register,LogoutView,verify,like_recipe,get_liked_recipes,editProfile,change_email,change_password,make_menu,blog

app_name = 'accounts'

urlpatterns = [
    path('login/',LoginView,name='login'),
    path('register/',Register,name='register'),
    path('logout/',LogoutView, name='logout'),
    path('verify/<slug>',verify,name='verify'),
    path('editprofile/',editProfile,name='edit_profile'),
    path('change_password/',change_password,name="change_password"),
    path('change_email/',change_email,name="change_email"),
    # path('check_email/',check_email,name="check_email"),
    path('make_menu/',make_menu, name="make_menu"),
    path("blog/", blog, name="blog"),
    path('like-recipe/',like_recipe, name="like_recipe"),
    path('liked_recipes/',get_liked_recipes, name="get_liked_recipes"),
    
]
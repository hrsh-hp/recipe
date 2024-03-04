from django.urls import path
from .views import home,contact

app_name = 'home'

urlpatterns = [
    path('',home,name='home'),
    path("contact/",contact,name="contact")
]
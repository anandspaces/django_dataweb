# new
from django.urls import path
from .views import home,users_profile

urlpatterns = [
    path('',home,name='home'),
    path('users-profile.html/',users_profile,name='users_profile'),
]
# new
from django.urls import path
from .views import home,users_profile,pages_faq,pages_contact,pages_register,pages_login,pages_error,pages_blank

urlpatterns = [
    path('',home,name='home'),
    path('users-profile/',users_profile,name='users_profile'),
    path('pages-faq/',pages_faq,name='pages_faq'),
    path('pages-contact/',pages_contact,name='pages_contact'),
    path('pages-register/',pages_register,name='pages_register'),
    path('pages-login/',pages_login,name='pages_login'),
    path('pages-error-404/',pages_error,name='pages_error'),
    path('pages-blank/',pages_blank,name='pages_blank'),
]
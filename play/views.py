from django.shortcuts import render
from .forms import CustomerForm
# Create your views here.
def home(request):
    template = 'index.html'
    return render(request,template,{})

def users_profile(request):
    template = 'users-profile.html'
    return render(request,template,{})

def pages_faq(request):
    template = 'pages-faq.html'
    return render(request,template,{})

def pages_contact(request):
    template = 'pages-contact.html'
    return render(request,template,{})

def pages_register(request):
    template = 'pages-register.html'
    form = CustomerForm
    return render(request,template,{'form':form})

def pages_login(request):
    template = 'pages-login.html'
    return render(request,template,{})

def pages_error(request):
    template = 'pages-error-404.html'
    return render(request,template,{})

def pages_blank(request):
    template = 'pages-blank.html'
    return render(request,template,{})

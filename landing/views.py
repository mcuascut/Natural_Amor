from django.shortcuts import render, get_object_or_404
from products.forms import SignUpForm
from django.contrib.auth import get_user, user_logged_in
from django.contrib.auth.models import AnonymousUser

def index(request): 
    
    first_name = " "
    user = request.user
    
    if request.user.is_authenticated: 
        first_name = user.first_name.capitalize()
        
    return render(request, "index.html", context={
        "first_name": first_name,
    })

def faq(request):
    
    first_name = " "
    user = request.user
    
    if request.user.is_authenticated: 
        first_name = user.first_name.capitalize()
    
    return render(request, "faq.html", context={
        "first_name": first_name,
    })

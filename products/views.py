from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def signup(request):
    
    form = SignUpForm()
     
    if request.method == "POST":
        
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "Registration successful.")

            print("POSTED")
            
            return redirect('/')
        messages.error(request, "Unsuccessful registration. Invalid Information.")

    else:
        
        form = SignUpForm()
    
    return render(request, template_name='signup.html', context={
        
        'form':form
        
        })
    
def loggingIn(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            		    
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
			
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect("/")
            
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
            
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={
        
        "form":form,
        
        })
    
def logOut(request):
    
    logout(request)
    messages.success(request, "You Have Logged Out!")
    return redirect("/")
    

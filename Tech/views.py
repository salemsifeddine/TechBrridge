from django.shortcuts import render
from.forms import  *
from django.contrib.auth.models import auth
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
# Create your views here.
import time
from time import *
from . import hw_sim


def main(request):
    
   

    return render(request,"pages/dash.html",{})

def chooseCar(request):
    return render(request,"pages/chooseCar.html",{})



def slidecars(request):
    return render(request,"pages/slidecars.html",{})


def login(request):
   
    if request.method != 'POST':
        form=LoginForm()

    else:
        form=LoginForm(data=request.POST)
       
        if form.is_valid():
            user = authenticate(
                    username=form.cleaned_data.get("username"),
                    password=form.cleaned_data.get("password"),
                )
            if user is not None:
                auth_login(request, user)
                return redirect("slidecars")

    context={"title":"Login","form":form}
    return render(request, "pages/login.html",context)

def logout(response):
    auth.logout(response)
    return redirect("home")

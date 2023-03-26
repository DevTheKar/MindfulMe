from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.http import HttpResponse
# from .models import Item
# Create your views here.

def index(request):
    # NEEDS INPUTS FROM BUTTONS AND STUFF
    return render(request, "main/index.html", {})

def profile(request):
    return render(request, "main/profile.html", {})

def signup(request):
    form=UserCreationForm()

    if request.method == "POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Account Created successfully")
            return redirect('main:login')


    context={
        'form':form
    }
    return render(request,'main/signup.html',context)

def login(request):
    return render(request, "main/login.html", {})

def affirm(request):
    return render(request, "main/affirm.html", {})

def journal(request):
    return render(request, "main/journal.html", {})

def track(request):
    return render(request, "main/track.html", {})

# def spotify(request):
#     return render(request, "MindfulMe/frontend/spotify.html", {})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewList
from .models import ToDoList, Item
from .models import Note
from .forms import NoteCreationForm,NoteUpdateForm

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

# JOURNAL-- DO NOT TOUCH
def journal(request):
    notes=Note.objects.all()
    form=NoteCreationForm()
    
    if request.method == "POST":
        form=NoteCreationForm(request.POST)

        if form.is_valid():
            note_obj=form.save(commit=False)
            note_obj.author=request.user
            note_obj.save()

            return redirect('main:home_page')

    context={
        'notes':notes,
        'form':form
    }
    return render(request,'main/journal.html',context)

def update(request,id):
    note_to_update=Note.objects.get(id=id)
    form=NoteUpdateForm(instance=note_to_update)

    if request.method == "POST":
        form=NoteUpdateForm(request.POST)

        if form.is_valid():
            note_to_update.title=form.cleaned_data["title"]
            note_to_update.description=form.cleaned_data["description"]

            note_to_update.save()

            return redirect('main:home_page')

    context={
        'note':note_to_update,
        'form':form
    }
    return render(request,'main/update.html',context)

def delete(request,id):
    note_to_delete=Note.objects.get(id=id)

    note_to_delete.delete()

    return redirect('main:home_page')

# DO NOT TOUCH ABOVE THIS


def track(request):
    return render(request, "main/track.html", {})

# James is working on this rn---------------------------------------

def list(request, id):
    ls = ToDoList.objects.get(id=id)

    if request.method == "POST":
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
    
            item.save()
    
        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
    
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")
    
    return render(request, "main/list.html", {"ls":ls})


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t) # adds the to do list to the current logged in user

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(request, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})
 
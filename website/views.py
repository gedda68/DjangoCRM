import math

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()
    # record_count = records.count()
    record_count = records.count()
    num_rows = math.ceil(record_count / 3)

    # check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            context = {"alert": "success"}
            return render(request, "home.html", context)
        else:
            messages.success(request, "There was an error logging, please try again...")
            context = {"alert": "warning"}
            return render(request, "home.html", context)
    else:
        return render(
            request,
            "home.html",
            {"records": records, "record_count": record_count, "num_rows": num_rows},
        )


# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have now been logged out...")
    context = {"alert": "success"}
    return render(request, "home.html", context)


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            context = {"alert": "success"}
            return render(request, "home.html", context)
            # return redirect('home')
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})


def user_record(request, pk):
    if request.user.is_authenticated:
        # lookup record
        user_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"user_record": user_record})
    else:
        messages.success(request, "You must logged into view the records!")
        context = {"alert": "warning"}
        return render(request, "home.html", context)


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "You have successfully deleted the record!")
        return redirect("home")
    else:
        messages.success(request, "You need to be logged in first!")
        return redirect("home")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "You have added a new record!")
                return redirect("home")
        else: 
            return render(request, "add_record.html", {"form": form})
    else:
        messages.success(request, "You must be logged on!")
        return redirect("home")
    
def update_record(request, pk):
        if request.user.is_authenticated:
            current_record = Record.objects.get(id=pk)
            form = AddRecordForm(request.POST or None, instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(request, "You have updated the record successfully!")
                return redirect("home")
            else:
                return render(request, "update_record.html", {"form": form})
        else:
            messages.success(request, "You must be logged on!")
            return redirect("home")



            
    
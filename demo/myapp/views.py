from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Bruker {user.username} ble opprettet. Du kan logge inn nå.")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "myapp/register.html", {"form": form})


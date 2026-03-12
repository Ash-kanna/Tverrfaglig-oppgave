from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")


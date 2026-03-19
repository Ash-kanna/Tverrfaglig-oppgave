from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Aktivitet

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


@login_required(login_url='login')
def member_list(request):
    members = User.objects.order_by('username')
    return render(request, "myapp/members.html", {"members": members})


@login_required(login_url='login')
def activity_list(request):
    aktiviteter = Aktivitet.objects.order_by('dato')
    return render(request, "myapp/activities.html", {"aktiviteter": aktiviteter})


def is_admin(user):
    return user.is_superuser or user.is_staff or user.username.lower() == 'admin'


@login_required(login_url='login')
@user_passes_test(is_admin)
def activity_create(request):
    if request.method == 'POST':
        navn = request.POST.get('navn', '').strip()
        beskrivelse = request.POST.get('beskrivelse', '').strip()
        dato = request.POST.get('dato')
        if navn and dato:
            Aktivitet.objects.create(navn=navn, beskrivelse=beskrivelse, dato=dato)
            messages.success(request, "Aktivitet opprettet.")
            return redirect('activities')
        messages.error(request, "Navn og dato er påkrevd.")
    return render(request, "myapp/activity_form.html")


@login_required(login_url='login')
@user_passes_test(is_admin)
def activity_delete(request, activity_id):
    aktivitet = get_object_or_404(Aktivitet, id=activity_id)
    if request.method == 'POST':
        aktivitet.delete()
        messages.success(request, "Aktivitet slettet.")
        return redirect('activities')
    return redirect('activities')


@login_required(login_url='login')
def activity_join(request, activity_id):
    aktivitet = get_object_or_404(Aktivitet, id=activity_id)
    aktivitet.deltakere.add(request.user)
    messages.success(request, "Du ble lagt til aktiviteten.")
    return redirect('activities')


@login_required(login_url='login')
def activity_leave(request, activity_id):
    aktivitet = get_object_or_404(Aktivitet, id=activity_id)
    aktivitet.deltakere.remove(request.user)
    messages.success(request, "Du meldte deg av aktiviteten.")
    return redirect('activities')


def is_admin(user):
    return user.is_superuser or user.is_staff or user.username.lower() == 'admin'


@login_required(login_url='login')
@user_passes_test(is_admin)
def member_delete(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        if target_user == request.user:
            messages.error(request, "Du kan ikke slette din egen bruker.")
        else:
            target_user.delete()
            messages.success(request, f"Bruker {target_user.username} er slettet.")
    return redirect('members')


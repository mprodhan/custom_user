from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from custom_user_app.models import LeUser
from custom_user_app.forms import LoginForm, Registration

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data["username"],
                password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage"))
                )
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def signup(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = LeUser.objects.create_user(
                name = data["name"],
                password = data["password"],
                display_name = data["display_name"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = Registration()
    return render(request, "generic_form.html", {"form": form})

def index(request):
    data = LeUser.objects.all()
    return render(request, "index.html", {"data": data})
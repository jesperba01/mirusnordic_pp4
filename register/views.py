from django.shortcuts import render, redirect
from .forms import RegisterForm

def get_register(request):
    template = "register/register.html"
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, template, context)

def login(request):
    template = "registration/login.html"
    context = {}
    return render(request, template, context)
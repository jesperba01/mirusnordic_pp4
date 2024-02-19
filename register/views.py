from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(response):
    template = "register/register.html"
    context = {"form":form}
    if response.method == "POST":
        form = RegisterForm(response.POST)
    if form.is_valid():
        form.save()
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, template, context)
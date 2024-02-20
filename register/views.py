from django.shortcuts import render, redirect
from .forms import RegisterForm

def get_register(request):
    template = "register/register.html"
    context = {"form":form}
    if request.method == "POST":
        form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(request, template, context)
from django.shortcuts import render, redirect
from .forms import RegisterForm

def get_register(request):
    template = "register/register.html"
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, template, context)
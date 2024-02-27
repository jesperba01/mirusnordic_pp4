from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from register.forms import RegisterForm

def get_register(request):
    template = "register/register.html"
    form = None  
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
            return redirect("home")
    else:  
        form = RegisterForm()  

    context = {"form": form}
    return render(request, template, context)
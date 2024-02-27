from django.shortcuts import render


def get_contact(request):
    template = "contact/contact.html"
    context = {}
    return render(request, template, context)

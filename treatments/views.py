from django.shortcuts import render
from .models import Treatment, Booking


def get_treatments(request):
    treatments = Treatment.objects.all()

    template = "treatments/treatments.html"
    context = {
        "treatments": treatments,
    }
    return render(request, template, context)


def get_bookings(request):
    bookings = Booking.objects.all()

    template = "treatments/bookings.html"
    context = {
        "bookings": bookings,
    }
    return render(request, template, context)

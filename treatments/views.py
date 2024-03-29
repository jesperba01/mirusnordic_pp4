from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Treatment, Booking
from .forms import BookingForm
from django.contrib import messages


def get_treatments(request):
    treatments = Treatment.objects.all()
    template = "treatments/treatments.html"
    context = {"treatments": treatments}
    return render(request, template, context)


@login_required
def get_bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Din bookning har sparats!.')
            return redirect('/dashboard')
    else:
        form = BookingForm(user=request.user)

    bookings = Booking.objects.filter(date__gte=timezone.now())

    template = "treatments/bookings.html"
    context = {
        "form": form,
        "bookings": bookings,
    }
    return render(request, template, context)

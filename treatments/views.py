from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Treatment, Booking
from .forms import BookingForm


def get_treatments(request):
    treatments = Treatment.objects.all()
    template = "treatments/treatments.html"
    context = {"treatments": treatments}
    return render(request, template, context)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Treatment, Booking
from .forms import BookingForm

@login_required
def get_bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)  # Pass the current user to the form
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the bookings page after successful booking
    else:
        form = BookingForm(user=request.user)  # Pass the current user to the form when initializing it

    # If a date is provided in the request, filter bookings for that date
    date = request.GET.get('date')
    if date:
        bookings = Booking.objects.filter(date=date)
    else:
        bookings = None
    
    template = "treatments/bookings.html"
    context = {
        "form": form,
        "bookings": bookings,  # Pass the filtered bookings to the template context
    }
    return render(request, template, context)
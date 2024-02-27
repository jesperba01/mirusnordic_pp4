from django.shortcuts import render, redirect
from treatments.models import Booking

def get_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated
    
    bookings = Booking.objects.filter(user=request.user, active=True)
    template = "dashboard/dashboard.html" 
    context = {'bookings': bookings}
    return render(request, template, context)


def cancel_booking(request, booking_id):
    # Retrieve the booking object
    booking = Booking.objects.get(pk=booking_id)
    
    # Perform the cancellation logic (e.g., set active=False)
    booking.active = False
    booking.save()

    # Redirect to the dashboard or any other page after cancellation
    return redirect('dashboard')
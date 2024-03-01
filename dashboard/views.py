from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from treatments.models import Booking
from .forms import EmailChangeForm

@login_required
def get_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated
    
    bookings = Booking.objects.filter(user=request.user, active=True)
    template = "dashboard/dashboard.html" 
    context = {'bookings': bookings}
    return render(request, template, context)

@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    
    print("Cancelling booking:", booking.id)
    booking.active = False
    booking.save()

    return redirect('dashboard')

@login_required
def change_email(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email has been updated successfully.')
            return redirect('dashboard')
    else:
        form = EmailChangeForm(instance=request.user)
    return render(request, 'dashboard/change-email.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the user's session to prevent them from being logged out
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been successfully updated.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/change_password.html', {'form': form})
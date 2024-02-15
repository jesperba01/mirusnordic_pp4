from django.urls import path
from . import views

urlpatterns = [
    path("treatments/", views.get_treatments, name="treatments"),
    path("bookings/", views.get_bookings, name="bookings"),
]

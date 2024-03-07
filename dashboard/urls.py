from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_dashboard, name="dashboard"),
    path(
        "cancel_booking/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
    path("change_email/", views.change_email, name="change_email"),
    path("change_password/", views.change_password, name="change_password"),
]

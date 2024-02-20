from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.get_register, name="register"),
]
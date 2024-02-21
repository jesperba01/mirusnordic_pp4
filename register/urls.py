from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_register, name="register"),
    path("accounts/login/", views.login, name="login"),
]
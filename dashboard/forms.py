from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class EmailChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email',)
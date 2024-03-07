from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class EmailChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email',)

class PasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
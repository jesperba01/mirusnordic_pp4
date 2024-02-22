from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'treatment']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.pop('readonly', None)  # Remove readonly attribute
        self.fields['date'].widget.attrs['class'] = 'datepicker'  # Add a CSS class for datepicker
        if user:
            self.user = user  # Store the user instance

    def save(self, commit=True):
        instance = super().save(commit=False)
        if hasattr(self, 'user'):
            instance.user = self.user  # Set the user field if it exists
        if commit:
            instance.save()
        return instance
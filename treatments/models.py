from django.db import models
from django.contrib.auth.models import User

class Treatment(models.Model):
    """
    A model to handle treatment types.
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    cost = models.PositiveIntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image_url = models.URLField(null=True, blank=True) 

    class Meta:
        ordering = ["cost"]

    def __str__(self):
        return self.name

class Booking(models.Model):
    """
    A model to handle the booking sessions.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, null=False, blank=False)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = [['user', 'date']]

    def __str__(self):
        return f"{self.user.username} - {self.date}"
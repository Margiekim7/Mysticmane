from django.db import models

# Create your models here.

from django.db import models


class Service(models.Model):
    """Model for services offered."""
    name = models.CharField(max_length=100)  # e.g., Smooth Shave
    description = models.TextField(blank=True, null=True)  # Optional detailed description

    def __str__(self):
        return self.name


class Barber(models.Model):
    """Model for barbers."""
    name = models.CharField(max_length=100)  # e.g., Zaki
    profile_image = models.ImageField(upload_to='barbers/', blank=True, null=True)  # Optional profile image
    experience = models.TextField(blank=True, null=True)  # Optional barber experience description

    def __str__(self):
        return self.name


class Appointment(models.Model):
    """Model for customer appointments."""
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # The service booked
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)  # The barber assigned
    name = models.CharField(max_length=100)  # Customer name
    phone = models.CharField(max_length=15)  # Customer phone number
    email = models.EmailField()  # Customer email
    date = models.DateField()  # Appointment date
    time = models.TimeField()  # Appointment time
    message = models.TextField(blank=True, null=True)  # Optional message from the customer

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"



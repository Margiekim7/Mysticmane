from django import forms
from mysticapp.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'stylist', 'image', 'message']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
from django import (forms)
from mysticapp.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

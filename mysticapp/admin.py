from django.contrib import admin
from mysticapp.models import User, Appointment, Message


# Register your models here.
admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(Message)
from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=50)
    yob = models.DateField()
    def __str__(self):
        return self.fullname

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateTimeField()
    stylist = models.CharField(max_length=50)
    message = models.TextField(max_length=100)
    def __str__(self):
        return self.name

class Message(models.Model):
    Name= models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=100)
    def __str__(self):
        return self.Name
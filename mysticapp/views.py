from django.shortcuts import render, redirect
from mysticapp.models import Appointment, Message

from mysticapp.forms import AppointmentForm


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def pricing(request):
    return render(request, 'pricing.html')


def contact(request):
    return render(request, 'contact.html')
def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == 'POST':
        mymessage=Message(
            Name= request.POST['name'],
            email = request.POST['email'],
            message= request.POST['message']
        )
        mymessage.save()
        return redirect('index')
    else:
        return render(request, 'contact.html')
def appointment(request):
   if request.method == 'POST':
      myappointment=Appointment(
          name= request.POST['name'],
          email= request.POST['email'],
          phone= request.POST['phone'],
          date= request.POST['datetime'],
          stylist= request.POST['stylist'],
          message= request.POST['message'],
      )
      myappointment.save()
      return redirect('index')
   else:
       return render(request, 'appointment.html')

def show(request):
    allappointments=Appointment.objects.all()
    return render(request,'show.html' ,{'appointments':allappointments})

def delete(request,id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')

# def edit(request,id):
#    editappointment=Appointment.objects.get(id=id)
#    return render(request, 'edit.html', {'appointment':editappointment})
#
# def update(request, id):
#    updateinfo = Appointment.objects.get(id=id)
#    form=AppointmentForm(request.POST, instance=updateinfo)
#    if form.is_valid():
#        form.save()
#        return redirect('/show')
#    else:
#        return render(request, 'edit.html')




def edit(request, id):
   editappointment = Appointment.objects.get(id=id)
   return render(request, 'edit.html', {'appointment':editappointment})

def update(request, id):
    updateinfo = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html')
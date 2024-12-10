from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from mysticapp.models import Appointment, Message
from mysticapp.forms import AppointmentForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def pricing(request):
    return render(request, 'pricing.html')

def blog(request):
    return render(request, 'blog.html')


def contact(request):
    if request.method == 'POST':
        try:
            mymessage = Message(
                Name=request.POST['name'],
                email=request.POST['email'],
                message=request.POST['message']
            )
            mymessage.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        except Exception as e:
            messages.error(request, 'There was an error sending your message.')
            return render(request, 'contact.html')
    return render(request, 'contact.html')


def appointment(request):
    if request.method == 'POST':
        try:
            myappointment = Appointment(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                date=request.POST.get('datetime'),  # Changed from 'date' to 'datetime'
                stylist=request.POST.get('stylist'),
                image=request.FILES.get('image'),
                message=request.POST.get('message'),
            )
            myappointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('show')
        except Exception as e:
            messages.error(request, f'Error booking appointment: {str(e)}')
            return render(request, 'appointment.html')
    return render(request, 'appointment.html')


def show(request):
    all_appointments = Appointment.objects.all().order_by('-date')
    return render(request, 'show.html', {'appointments': all_appointments})


def delete(request, id):
    try:
        appoint = get_object_or_404(Appointment, id=id)
        appoint.delete()
        messages.success(request, 'Appointment deleted successfully!')
    except Exception as e:
        messages.error(request, f'Error deleting appointment: {str(e)}')
    return redirect('show')


def edit(request, appointment_id):
    try:
        editappointment = get_object_or_404(Appointment, id=appointment_id)
        return render(request, 'edit.html', {'appointment': editappointment})
    except Exception as e:
        messages.error(request, f'Error retrieving appointment: {str(e)}')
        return redirect('show')


def update(request, appointment_id):
    updateinfo = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=updateinfo)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Appointment updated successfully!')
                return redirect('show')
            except Exception as e:
                messages.error(request, f'Error updating appointment: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors in the form.')

    return render(request, 'edit.html', {'appointment': updateinfo})
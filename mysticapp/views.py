from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def blog(request):
    return render(request,'blog.html')
def singleblog(request):
    return render(request,'single-blog.html')

def elements(request):
    return render(request,'elements.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def pricing(request):
    return render(request, 'pricing.html')
def appointment(request):
    return render(request, 'appointment')



from django.urls import path
from . import views

app_name = 'mysticapp'  # Add namespace for the app

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('pricing/', views.pricing, name='pricing'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('appointments/', views.show, name='show'),
    path('appointments/delete/<int:appointment_id>/', views.delete, name='delete'),
    path('appointments/edit/<int:appointment_id>/', views.edit, name='edit'),
    path('appointments/update/<int:appointment_id>/', views.update, name='update')
]
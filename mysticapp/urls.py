

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('pricing/', views.pricing, name='pricing'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update, name='update')
]

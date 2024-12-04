

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('singleblog/', views.singleblog, name='single_blog'),
    path('contact/', views.contact, name='contact'),
    path('element/', views.elements, name='elements'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.index, name='blog'),
    path('singleblog/', views.index, name='single_blog'),
    path('contact/', views.index, name='contact'),
    path('element/', views.index, name='elements'),
    path('about/', views.index, name='about'),
    path('service/', views.index, name='service'),
]

from django.urls import path
from . import views

# Define a list of url patterns
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('our-pets/', views.our_pets, name='our_pets'),
]
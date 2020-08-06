from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.landing, name="about"),
    path('contact/', views.contact, name="contact"),
    path('impressum/', views.impressum, name="impressum"),
    path('legal/', views.legal, name="legal"),
]

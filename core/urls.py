from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="about"),
    path('contact/', views.contact, name="contact"),
    path('impressum/', views.impressum, name="impressum"),
    path('legal/', views.legal, name="legal"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_index, name="projects"),
    path('<slug:slug>/', views.projects_detail, name="projects_detail"),
]

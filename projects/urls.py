from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_index, name="projects"),
    path('<int:pk>/', views.projects_detail, name="projects_detail"),
]

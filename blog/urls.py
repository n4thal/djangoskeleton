from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

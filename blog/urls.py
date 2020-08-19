from django.urls import path
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    path('', views.post_index, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('feed/rss/', LatestPostsFeed(), name='post_feed'),
]

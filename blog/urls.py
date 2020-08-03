from django.urls import path
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    path('feed/rss', LatestPostsFeed(), name='post_feed'),
]

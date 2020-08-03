from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]

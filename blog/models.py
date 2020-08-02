from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    last_modified = models.DateTimeField(auto_now=True)
    summary = models.TextField(default='summary', max_length=200)
    content = models.TextField(default='content')
    publication_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title

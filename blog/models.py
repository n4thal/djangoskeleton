from django.db import models
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

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['publication_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='static/img')
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("projects_detail", kwargs={"technology": str(self.technology)})

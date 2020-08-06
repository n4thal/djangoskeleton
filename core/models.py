from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postcode = models.IntegerField()
    city = models.CharField(max_length=31)
    mail = models.EmailField()
    phone = models.CharField(max_length=15)
    hook = models.CharField(max_length=511)
    description = models.CharField(max_length=2000)
    history = models.CharField(max_length=2000)
    call_to_action = models.CharField(max_length=127)


class MetaInfo(models.Model):
    description = models.CharField(max_length=511)
    keywords = models.CharField(max_length=2000)


class Core(models.Model):
    pass


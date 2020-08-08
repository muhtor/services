from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    language = models.CharField(max_length=3)

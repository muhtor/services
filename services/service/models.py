from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    language = models.CharField(max_length=3)


class Post(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text[:10]

from django.db import models

# Create your models here.


class Post(models.Model):
    writer = models.CharField(max_length=30)
    content = models.TextField()

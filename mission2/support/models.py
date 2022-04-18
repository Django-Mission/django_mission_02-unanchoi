from django.db import models

# Create your models here.


class Faq(models.Model):
    question = models.TextField()
    category = models.CharField(
        max_length=30,
        default='mission',
        choices=[
            ('User', 'User'),
            ('mission', 'mission'),
            ('etc', 'etc')
        ]
    )
    answer = models.TextField()
    writer = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    editor = models.CharField(max_length=50)
    edited_at = models.DateTimeField(auto_now=True)

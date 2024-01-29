from django.db import models

# Create your models here.

# pylint: disable=E1101
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('A', 'ACTION'),
    ('D', 'DRAMA')
    ('C', 'COMEDY')
    ('R', 'ROMANCE')
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')

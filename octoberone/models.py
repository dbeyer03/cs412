#migration/models.py
# define data models (objects) for use in the blog application
from django.db import models

# Create your models here.
class Article(models.Model):
  '''Encapsulat the data for an Article by same author.'''

  # data attributes:
  title = models.TextField(blank=False)
  author = models.TextField(blank=False)
  text = models.TextField(blank=False)
  published = models.DateTimeField(auto_now=True)
  image_url = models.URLField(blank=True)

  def __str__(self):
    '''Return a string representation of this Articls.'''
    return f"{self.title} {self.author}"
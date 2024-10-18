from django.db import models
from django.urls import reverse ## NEW

# Create your models here.
class Profile(models.Model):
  first_name = models.TextField(blank=False)
  last_name = models.TextField(blank=False)
  city = models.TextField(blank=False)
  email_address = models.TextField(blank=False)
  profile_image_url = models.URLField(blank=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  
  def get_status_messages(self):
    '''Retrieve status message for this Profile.'''
    message = StatusMessage.objects.filter(profile=self)
    return message

  def get_absolute_url(self):
    '''Return the URL to redirect to after successfully submitting form.'''
    return reverse('show_profile',kwargs={'pk': self.pk})


class StatusMessage(models.Model):
  text = models.TextField(blank=False)
  timestamp = models.DateTimeField(auto_now=True)
  profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
  
  def get_images(self):
    '''Retrieve all images for this Status Message.'''
    images = Image.objects.filter(status_message=self)
    return images

  def __str__(self):
    '''Return a string representation of this object.'''
    return f'{self.text} {self.timestamp}'

class Image(models.Model):
  image_file = models.ImageField(blank=True) # an actual image
  status_message = models.ForeignKey("StatusMessage", on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.timestamp}'
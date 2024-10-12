from django.db import models

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
  


class StatusMessage(models.Model):
  text = models.TextField(blank=False)
  timestamp = models.DateTimeField(auto_now=True)
  profile = models.ForeignKey("profile", on_delete=models.CASCADE)

  def __str__(self):
    '''Return a string representation of this object.'''
    return f'{self.profile} {self.text}'
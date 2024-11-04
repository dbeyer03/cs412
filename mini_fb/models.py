from django.db import models
from django.urls import reverse ## NEW
from django.contrib.auth.models import User ## NEW
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
  first_name = models.TextField(blank=False)
  last_name = models.TextField(blank=False)
  city = models.TextField(blank=False)
  email_address = models.TextField(blank=False)
  profile_image_url = models.URLField(blank=True)
  #used to store login info for profile user.
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  
  def get_status_messages(self):
    '''Retrieve status message for this Profile.'''
    message = StatusMessage.objects.filter(profile=self)
    return message

  def get_absolute_url(self):
    '''Return the URL to redirect to after successfully submitting form.'''
    return reverse('show_profile',kwargs={'pk': self.pk})
  
  def get_friends(self):
    '''Retrieve friends for this Profilie.'''
    all_friends = []

    friends1 = Friend.objects.filter(profile1=self)
    for f1 in friends1:
      if f1.profile2 is not None:
        all_friends.append(f1.profile2)

    friends2 = Friend.objects.filter(profile2=self)
    for f2 in friends2:
      if f2.profile1 is not None:
        all_friends.append(f2.profile1)

    return all_friends

  def add_friend(self, other):
    '''Add friends to this profile.'''

    if self != other:
      all_friends = Friend.objects.all()
      if (all_friends.filter(profile1=self,profile2=other).exists() == False) and (all_friends.filter(profile1=other,profile2=self).exists() == False):
        new_friend = Friend.objects.create(profile1=self,profile2=other)
        new_friend.save()
    return

  def get_friend_suggestions(self):
    '''Returns a list of possible friends for a profile.'''
    all_friends = Profile.get_friends(self)
    all_profiles = Profile.objects.all()
    suggested_fr = []

    for p in all_profiles:
      if (p not in all_friends) and (p != self):
        suggested_fr.append(p)

    return suggested_fr

  def get_news_feed(self):
    '''returns list of all StatusMessages for this profile
        and friends of this profile.'''

    #my own status_messages.
    my_status = Profile.get_status_messages(self)

    #my friends' status messages.
    all_friends = Profile.get_friends(self)
    all_status = my_status
    for f in all_friends:
      f_status = Profile.get_status_messages(f)
      all_status = all_status.union(f_status)
    
    ordered_fs = all_status.order_by('-timestamp')

    return ordered_fs

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 

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

class Friend(models.Model):
  profile1 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile1",  blank=True, null=True)
  profile2 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile2",  blank=True, null=True)
  timestamp = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.profile1} and {self.profile2}'

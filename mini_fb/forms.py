from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
  '''A form to create Profile data.'''
  first_name = forms.CharField(label="First Name", required=True)
  last_name = forms.CharField(label="Last Name", required=True)
  city = forms.CharField(label="City", required=True)
  email_address = forms.CharField(label="Email Address", required=True)
  profile_image_url = forms.ImageField(label="Profile Image", required=True)


  class Meta:
    model = Profile

    fields = ['first_name','last_name','city','email_address','profile_image_url']
from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
  '''A form to create Profile data.'''
  first_name = forms.CharField(label="First Name", required=True)
  last_name = forms.CharField(label="Last Name", required=True)
  city = forms.CharField(label="City", required=True)
  email_address = forms.CharField(label="Email Address", required=True)
  profile_image_url = forms.URLField(max_length=10000, label="Profile Image", required=True, widget=forms.TextInput(attrs={'placeholder': 'No URLs greater than 200 characters.', 'style': 'min-width: 150px; max-width: 500px; width: 190%;'}))


  class Meta:
    model = Profile
    fields = ['first_name','last_name','city','email_address','profile_image_url']

class CreateStatusMessageForm(forms.ModelForm):
  '''A form to create Status Message forms.'''
  text = forms.CharField(label="Status Message", required=True, widget=forms.Textarea(attrs={'placeholder': 'Status Message', 'style': 'width: 90%; max-width: 900px; height: 150px;;'}))

  class Meta:
    model = StatusMessage 
    fields = ['text']
  
class UpdateProfileForm(forms.ModelForm):
  city = forms.CharField(label="City", required=True)
  email_address = forms.CharField(label="Email Address", required=True)
  profile_image_url = forms.URLField(max_length=10000, label="Profile Image", required=True, widget=forms.TextInput(attrs={'placeholder': 'No URLs greater than 200 characters.', 'style': 'min-width: 150px; max-width: 500px; width: 190%;'}))

  class Meta:
    model = Profile 
    fields = ['city','email_address','profile_image_url']
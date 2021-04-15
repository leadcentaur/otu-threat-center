from django import forms
from django.contrib.auth.models import User
from .models import Profile


# no need for a registration form here as this is handled by google auth, we will use the template provided by all-auth
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    email.disabled = True

    class Meta:
        model = User
        fields = ['email']

# allow the user to modify their username and profile pic
class ProfileUpdateForm(forms.ModelForm):
    username = forms.CharField()
    username.disabled = True
    class Meta:
        model = Profile
        fields = ['img', 'username']

class SetUserNameUponSignup(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username']

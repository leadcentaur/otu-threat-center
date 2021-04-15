from django import forms
from django.contrib.auth.models import User
from .models import vpnUser

class VPNDisplayForm(forms.ModelForm):
    class Meta:
        model = vpnUser
        model.vpn_password.disabled = True
        fields = ['user']

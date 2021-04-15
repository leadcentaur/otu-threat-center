from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os

# CONSTs
password_length = int(os.getenv('VPN_PASSWORD_LENGTH', default=12))
vpn_userid_length = int(os.getenv('VPN_USERID_LENGTH', default=9))

# Model for the a vpn user
class vpnUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # The user's vpn password as generated in the views.py function 's_random_password'
    vpn_password = models.CharField(max_length=password_length)

    # opvn file for the user. This can also be populated with a path to a single vpn file for all users
    #   depending on the prefered ovpn setup
    vpn_file = models.FileField(upload_to='ovpnfiles/')

    # The user's id for the vpn. We use length 9 as is done with the Ontario Tech student ids (e.g., 100-xx-xx-xx)
    vpn_id = models.CharField(max_length=vpn_userid_length)

    # Last login time, this should be modified on the vpn service side, for now it is just a timezone.now call
    last_login = models.DateTimeField(default=timezone.now)

    # String cast calls should return the user's username
    def __str__(self):
        return f"{self.user.username}"
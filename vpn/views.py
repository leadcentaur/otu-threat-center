from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VPNDisplayForm
from .models import vpnUser
import string
from random import SystemRandom
import os
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import user_passes_test


def legal_check(user):
    if user.legal.terms_accepted:
        return True
    raise PermissionDenied

# CONSTs
password_length = int(os.getenv('VPN_PASSWORD_LENGTH', default=12))

# Generate a random 12 char alpha-numeric password for the user's vpn password
def s_random_password(size=password_length, chars=string.ascii_letters + string.digits):
    return ''.join(SystemRandom().choice(chars) for i in range(size))


# Generate credentials for a user for the vpn service. Passwords are randomly generated. The vpn file path is left
#   as a default value and should be altered once the vpn service is designed an implemented

def generate_credentials(user):
    vpn_password = s_random_password()
    vpn_file = 'filepath'
    return vpn_password, vpn_file


# This function handles the GETs and POSTs to the vpn page.

@login_required
@require_http_methods(["GET", "POST"])
@user_passes_test(legal_check)
def vpn(request):
    # A POST represents a user requesting the generation of new credentials. We generate and store their new credentials
    #   and then redirect them to the vpn page triggering a GET on this view
    if request.method == "POST":
        vpn_password, vpn_file = generate_credentials(request.user)
        vpnUser.objects.filter(user=request.user).update(vpn_password=vpn_password, vpn_file=vpn_file)
        return redirect('vpn')

    # This section handles GETs.
    # We query the db for the user's credentials and return them for front end use. If a user does not exist in the
    #   vpn user model (i.e., they have never generated credentials), we return defaults requesting that they generate
    #   credentials.
    else:
        vpnUser_credentials, exists = vpnUser.objects.get_or_create(user=request.user,
                                                                    defaults={
                                                                              "vpn_password": 'Please request a password',
                                                                              "vpn_file": '/'})

        # The user's vpn id, password, file and timestamp, formatted for front end use
        context = {
            'vpn_user': vpnUser_credentials.user,
            'vpn_password': vpnUser_credentials.vpn_password,
            'vpn_file': vpnUser_credentials.vpn_file,
            'vpn_last_login': vpnUser_credentials.last_login
        }
    return render(request, 'vpn/vpn_home.html', context)

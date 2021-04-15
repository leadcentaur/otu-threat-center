# TODO

Remaing items for deployment.

### Todo

- [ ] Production staging DEBUG setting in src/settings.py come production deployment.
- [ ] Set environment vars for configuration - create a gmail service account.
- [ ] Change the static file handling for the site, for serving profile images and vpn file, this might be useful at some point:
    - https://docs.djangoproject.com/en/3.1/howto/static-files/deployment/
- [ ] Create or use an existing GoogleAuth Project via the Google Console API with the domain set to ontariotechu domain only.
    - https://support.google.com/cloud/answer/6158849?hl=en
- [ ] Modify Reports and Target models to include different Assets and Faculty owners, this includes the adjustment of any or all models.
- [ ] Add legal agreement text overview.html 
- [ ] SMTP is configured on Port 587, firewall rules may have to be adjusted etc
    
### OAuth2 Client ID configuration for testing in a local environment:

- https://console.cloud.google.com/

Authorized JavaScript origins
- http://localhost:8000

Authorized redirect URIs
- http://127.0.0.1:8000/accounts/google/login/callback/
- http://127.0.0.1:8000/complete/google-oauth2/
   



from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.core.validators import validate_image_file_extension

class Legal(models.Model):
    legal_id = models.AutoField(primary_key=True)
    terms_accepted = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disclaimer_text = models.TextField(default="Employees are expressly required not to make defamatory statements and not to infringe or authorize any infringement of copyright or any other legal right by email communications. Employees who receive such an email must notify their supervisor immediately.")
    email_confirmation = models.EmailField(null=True, blank=True, max_length=254)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=42)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics', validators=[validate_image_file_extension])

    def __str__(self):
        return f'{self.user.email} Profile'

    # here we overwrite the save method to decrease the size of the image being uploaded
    # smaller image = faster site = faster user experience
    # max images (model)message -> report images
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        i = Image.open(self.img.path)
        if i.height > 300 or i.width > 300:
            output_size = (300, 300)
            i.thumbnail(output_size)
            i.save(self.img.path)

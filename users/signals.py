# will get fired when an object is saved, get a post save sginal when a user is creates (could also apply to prd)
# signal requires sender and receiver
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save, post_delete, pre_delete, pre_save, post_init
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib import messages
from .models import Profile, Legal
from src.settings import BASE_DIR
import os

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Legal.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    messages.success(request, f"You have logged in successfully. Welcome {request.user.email}")

# if the account is deleted we need to clean up the user profile
@receiver(pre_delete, sender=Profile)
def handle_files_on_account_delete(sender, instance, **kwargs):
    print(instance.img.url)
    if instance.img.url != '/media/default.jpg':
        os.remove(str(BASE_DIR) + instance.img.url)

@receiver(pre_save, sender=Profile)
# handles uer upload, if the user uploads a picture we remove the old one.
def handle_profile_pic_upload(sender, instance, **kwargs):
    if not instance._state.adding:
        new_file = instance.img
        old_file = sender.objects.get(pk=instance.pk).img

        if old_file.url != '/media/default.jpg' and old_file != new_file:
            os.remove(old_file.path)


# need a way to remove the old profile picture when a new one has been uploaded.


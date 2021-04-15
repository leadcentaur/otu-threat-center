from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save, post_delete, pre_delete, pre_save
from main.models import Report
from django.dispatch import receiver
from django.contrib import messages
from .models import Profile
from users.models import Legal
from src.settings import BASE_DIR
import os


# Handles the deletion of the report, deletes the images associated with the report.
@receiver(post_delete, sender=Report)
def handle_report_deletion(sender, instance, **kwargs):
    img_fields = ['img_a', 'img_b']
    for key, value in vars(instance).items():
        if key in img_fields:

            # check if the images currently populated are not the default image
            if getattr(instance, key).url != '/media/default.jpg':
                print("Deleting: ", str(BASE_DIR) + '/media/' + str(getattr(instance, key)))
                os.remove(str(BASE_DIR) + '/media/' + str(getattr(instance, key)))


# Handles the report image updating, that is if the user decides to change one of their screen shots
# Then it woll delete the previous one.
@receiver(pre_save, sender=Report)
def handle_report_update(sender, instance, **kwargs):
    img_fields = ['img_a', 'img_b']

    # check if the state of the instance is not in adding
    if not instance._state.adding:
        old_imgs = sender.objects.get(pk=instance.pk)
        for key, value in vars(old_imgs).items():
            if key in img_fields:

                # load the old image and verify that it is not the place holder image
                old_image = getattr(sender.objects.get(pk=instance.pk), key)
                if old_image != getattr(instance, key) and old_image.url != '/media/default.jpg':
                    print("Old image url", old_image.url)
                    os.remove(old_image.path)

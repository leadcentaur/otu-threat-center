from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone
from main.models import Report

#  This message model defines the storage of messages attached to a particular report
#    Messages can be attached not a report either by the submitter or by an admin
#    Messages contain a sender (a foreign key to the user that represents the student who created the report)
#                     a report (a foreign key to the report the message is in relation to)
#                     message_text (A text field holding the text content of a message)
#                     message_image (a file field for a single image uploaded as part of a message)
#                     message_timestamp (A datetime timestamp of the time the message was created)
class Message(models.Model):
     sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
     report = models.ForeignKey(Report, on_delete=models.CASCADE)
     message_text = models.TextField()
     message_image = models.FileField(upload_to='../media/message_pics', blank=True)
     message_timestamp = models.DateTimeField(default=timezone.now)

# This function deletes the image associated with a message when the message object is deleted (or when the report
#    to which the messages are associated is deleted)
@receiver(post_delete, sender=Message)
def submission_delete(sender, instance, **kwargs):
    instance.message_image.delete(False)
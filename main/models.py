from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.utils import timezone
from django.urls import reverse
from django.core.validators import validate_image_file_extension

# add additional assets where we see fit
ASSET_CHOICES = (
    ('cloud_web_panel', 'Cloud Web Panel'),
    ('hrl_subnet', 'HRL Subnet'),
    ('otu_Website', 'OTU Website'),
    ('other', 'Other')
)
STATUS_CHOICES = (
    ("accepted", "Accepted"),
    ("pending_review", "Pending review"),
    ("closed", "Closed"),
)
# compile a list of all the faculties
OWNER_CHOICES = (
    ('fbit', 'FBIT'),
    ('otu', 'OTU'),
    ('ssh', 'SSH')
)
# pulled form owasp top 10
CLASSIFICATION_CHOICES = (
    ('xss', 'Cross-Site Scripting (XSS)'),
    ('injection', 'Injection'),
    ('broken_auth', 'Broken Authentication'),
    ('broken_ac', 'Broken Access Control'),
    ('sec_misconfiguration', 'Security Misconfiguration'),
    ('ssrf', 'Server Side Request Forgery (SSRF)'),
    ('logging_monitoring', 'Insufficient Logging and Monitoring'),
    ('insecure_deserialization', 'Insecure Deserialization'),
    ('sensitive_data_exposure', 'Sensitive Data Exposure'),
    ('rce', 'Remote Code Execution (RCE)'),
)
SEVERITY_CHOICES = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ('very_high', 'Very High'),
    ('critical', 'Critical')
)


class Report(models.Model):
    points = models.IntegerField(default=0, blank=True)
    title = models.CharField(max_length=128)
    details = models.TextField(max_length=5012)

    id = models.AutoField(primary_key=True)

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default='high'
    )

    asset = models.CharField(choices=ASSET_CHOICES, max_length=20)

    status = models.CharField(
        choices=STATUS_CHOICES,
        default='pending_review',
        max_length=32,
        blank=True
    )

    date_submitted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    classification = models.CharField(choices=CLASSIFICATION_CHOICES, max_length=32)

    '''
    img_a = models.ImageField(default='default.jpg', upload_to='report_pics', validators=[validate_image_file_extension])
    img_b = models.ImageField(default='default.jpg', upload_to='report_pics', validators=[validate_image_file_extension])
    '''

    class Meta:
        pass

    def __str__(self):
        return f'{self.title} Report'

    def get_absolute_url(self):
        return reverse('overview')


class Target(models.Model):
    asset = models.CharField(max_length=20, choices=ASSET_CHOICES)
    iprange = models.CharField(max_length=132)
    ports = models.CharField(max_length=132)
    hostname = models.CharField(max_length=253)

    owner = models.CharField(
        max_length=4,
        choices=OWNER_CHOICES
    )

    class Meta:
        pass

    def __str__(self):
        return f'{self.hostname}'

    def get_absolute_url(self):
        return reverse('targets')

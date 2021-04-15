from django import forms
from main.models import Report
from users.models import User, Legal, Profile


class ReportSubmitForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'details', 'asset', 'classification', 'severity']


class LegalForm(forms.ModelForm):
    email_confirmation = forms.EmailField(required=True)

    class Meta:
        model = Legal
        fields = ['email_confirmation']

class SetUserNameUponSignup(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username']

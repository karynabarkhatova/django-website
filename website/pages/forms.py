from django import forms
from django.utils import timezone

TOPIC_CHOICES = [
    ('Make an appointment', 'Make an appointment'), 
    ('Online consultation', 'Online consultation'), 
    ('Enrollment in a sarcasm course', 'Enrollment in a sarcasm course'), 
    ('Just wanna piss you off', 'Just wanna piss you off'),
    ]


class Contact_Form(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    topic = forms.ChoiceField(widget=forms.Select, choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea, max_length=500)
    response = forms.BooleanField(required=False)
    
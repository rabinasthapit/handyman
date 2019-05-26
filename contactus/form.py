from django.forms import ModelForm
from django import forms
from .models import ContactUs

class ContactUsForm(ModelForm):
    class Meta:
        model=ContactUs
        fields='__all__'

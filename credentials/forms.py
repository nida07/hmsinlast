from django import forms
from .models import biometric

class BiometricForm(forms.ModelForm):
    class Meta:
        model = biometric
        fields = ['height','weight','bloodpressure'] # This includes all fields in the form

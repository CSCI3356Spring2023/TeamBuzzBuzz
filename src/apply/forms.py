from django import forms

from .models import ApplyModel

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplyModel
        fields = [
            'additional_information'
        ]
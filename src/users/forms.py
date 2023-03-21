from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    gpa = forms.DecimalField(max_digits=3, decimal_places=2)
    year = forms.IntegerField(min_value=2023)  # Add the year field
    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'gpa', 'year', 'is_staff']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    gpa = forms.DecimalField(max_digits=3, decimal_places=2)
    year = forms.IntegerField(min_value=2023)  

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'gpa', 'year']

    
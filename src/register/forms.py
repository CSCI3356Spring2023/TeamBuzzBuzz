from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    gpa = forms.DecimalField(min_value=0.0, max_value=4.0, decimal_places=2)
    user_type = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'gpa', 'user_type']
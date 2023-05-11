from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

RELATIONSHIP_CHOICES = (
    ("BS", "Major BS"),
    ("BA", "Major BA"),
    ("MIN", "Minor"),
)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    eagle_ID = forms.IntegerField(min_value=00000000)
    gpa = forms.DecimalField(max_digits=3, decimal_places=2, required=False)
    year = forms.IntegerField(
        min_value=2023, required=False)  # Add the year field
    is_staff = forms.BooleanField(required=False)
    relationship_to_department = forms.ChoiceField(
        choices=RELATIONSHIP_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2',
                  'first_name', 'last_name', 'eagle_ID', 'relationship_to_department', 'gpa', 'year', 'is_staff']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    gpa = forms.DecimalField(max_digits=3, decimal_places=2)
    year = forms.IntegerField(min_value=2023)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'gpa', 'year']

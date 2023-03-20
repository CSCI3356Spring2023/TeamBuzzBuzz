# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class SignUpForm(UserCreationForm):
# 	email = forms.EmailField()

# 	CLASSCHOICES = (
# 		(1, '    '),
# 		(2, '2023'),
# 		(3, '2024'),
# 		(4, '2025'),
# 		(5, '2026')
# 	)
# 	year = forms.ChoiceField(choices = CLASSCHOICES, widget = forms.Select)

# 	gpa = forms.DecimalField()

# 	CHOICES = (
# 		(1, '    '),
# 		(2, 'Student'),
# 		(3, 'Professor'),
# 		(4, 'Admin')
# 	)
# 	position = forms.ChoiceField(choices = CHOICES, widget = forms.Select)

# 	class Meta:
# 		# change this to our model
# 		model = User
# 		fields = ('username', 'email', 'password1', 'password2', 'year', 'gpa')


from django import forms
from .models import SignUp 

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = [
        	'name', 
        	'email',
        	'password',
        	'position',
        	'year', 
        	'gpa'
        ]
        widgets = {
        	'password': forms.PasswordInput()
        }




# from django import forms

# class LoginForm(forms.Form):
# 	email = forms.EmailField()
# 	password = forms.CharField(widget = forms.TextInput())


from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
        	'email',
        	'password'
        ]
from django import forms

class SignUpForm(forms.Form):
	name = forms.CharField(widget = forms.TextInput())
	email = forms.EmailField()
	password = forms.CharField(widget = forms.TextInput())

	CLASSCHOICES = (
		(1, '    '),
		(2, '2023'),
		(3, '2024'),
		(4, '2025'),
		(5, '2026')
	)
	year = forms.ChoiceField(choices = CLASSCHOICES, widget = forms.Select)

	gpa = forms.DecimalField()

	CHOICES = (
		(1, '    '),
		(2, 'Student'),
		(3, 'Professor'),
		(4, 'Admin')
	)
	position = forms.ChoiceField(choices = CHOICES, widget = forms.Select)

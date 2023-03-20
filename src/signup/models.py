from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignUp(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=60)
	email = models.EmailField()
	password = models.CharField(max_length=60)

	CHOICES = (
		('1', 'Student'),
		('2', 'Professor'),
		('3', 'Admin')
	)
	position = models.CharField(choices = CHOICES, max_length = 1)

	CLASSCHOICES = (
		('1', '2023'),
		('2', '2024'),
		('3', '2025'),
		('4', '2026')
	)
	year = models.CharField(choices = CLASSCHOICES, max_length = 1)

	gpa = models.DecimalField(decimal_places = 2, max_digits = 3, default = 0.0)
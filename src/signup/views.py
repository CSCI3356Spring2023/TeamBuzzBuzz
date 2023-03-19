from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SignUpForm

# Create your views here.
def signup_view(request, *args, **kwargs):
	my_form = SignUpForm()
	context = {
		'form': my_form
	}
	return render(request, 'signup/signup.html', context )



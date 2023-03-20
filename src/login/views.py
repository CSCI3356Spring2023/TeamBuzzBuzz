from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import LoginForm
from signup.models import SignUp

# Create your views here.
def login_view(request, *args, **kwargs):
	if request.method == 'GET':
		form = LoginForm(request.GET or None)
		if form.is_valid():
			emailinput = form.cleaned_data.get('email')
			correctInfo = SignUp.objects.get(email = emailinput)
			print(correctInfo)
	else:
		form = LoginForm()
	context = {
		'form': form
	}
	return render(request, 'login/login.html', context )
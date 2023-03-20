from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm
from signup.models import SignUp
from django.contrib import messages

# Create your views here.
def login_view(request, *args, **kwargs):
	if request.method == 'GET':
		form = LoginForm(request.GET or None)
		if form.is_valid():
			emailinput = form.cleaned_data.get('email')
			passwordinput = form.cleaned_data.get('password')
			try:
				correctInfo = SignUp.objects.get(email = emailinput)
				userType = correctInfo.position
				if emailinput == correctInfo.email and passwordinput == correctInfo.password:
					messages.success(request, f'Login success for {emailinput}!')
					if userType == '1':
						return redirect('student')
					elif userType == '2':
						return redirect('professor')
					else:
						return redirect('bcadmin')
				else:
					form = LoginForm()
					messages.warning(request, f'Login failed for {emailinput}!')
			except:
				form = LoginForm()
				messages.warning(request, f'Login failed for {emailinput}!')
	else:
		form = LoginForm()

	context = {
		'form': form
	}
	return render(request, 'login/login.html', context )
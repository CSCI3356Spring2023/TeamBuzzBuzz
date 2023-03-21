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
					return redirect('landing', correctInfo.email, userType)
						
					# use this code if we want 3 seperate landing pages
					# if userType == '1':
					# 	return redirect('student', data = data)
					# elif userType == '2':
					# 	return redirect('professor', data = data)
					# else:
					# 	return redirect('bcadmin', data = data)

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
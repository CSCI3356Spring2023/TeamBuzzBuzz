from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def signup_view(request, *args, **kwargs):
	my_form = SignUpForm()
	context = {
		'form': my_form
	}
	return render(request, 'signup/signup.html', context )


# def signup_view(request, *args, **kwargs):
# 	if request.method == 'POST':
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			form.save() # This saves the user to the database
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, f'Account created for {username}!')
# 			return redirect('home')
# 	else:
# 		form = SignUpForm()
# 	context = { 'form': form }
# 	return render(request, 'signup/signup.html', context )



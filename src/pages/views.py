from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def login_view(request, *args, **kwargs):
	user = User.objects.get(email='abc@gmail.com')
	# return HttpResponse('<h1>Hello World</h1>')
	context = {
		'email': user.email,
	}
	return render(request, 'login.html', context)


def signup_view(request, *args, **kwargs):
	# return HttpResponse('<h1>Hello World</h1>')
	context = {}
	return render(request, 'signup.html', context)

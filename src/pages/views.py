from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def login_view(request, *args, **kwargs):
	# return HttpResponse('<h1>Hello World</h1>')
	context = {
		'email': "exampleemail@gmail.com",
	}
	return render(request, 'login.html', context)

def add_course_view(request, *args, **kwargs):
    context = {
		
	}
    return render(request, 'add_course.html', context)
    
def signup_view(request, *args, **kwargs):
	# return HttpResponse('<h1>Hello World</h1>')
	context = {}
	return render(request, 'signup.html', context)

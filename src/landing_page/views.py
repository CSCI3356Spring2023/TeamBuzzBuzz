from django.shortcuts import render
from login.forms import LoginForm
# Create your views here.

def student_view(request, *args, **kwargs):
	context = {}
	return render(request, 'landing/student.html', context)

def professor_view(request, *args, **kwargs):
	context = {}
	return render(request, 'landing/professor.html', context)

def admin_view(request, *args, **kwargs):
	context = {}
	return render(request, 'landing/admin.html', context)


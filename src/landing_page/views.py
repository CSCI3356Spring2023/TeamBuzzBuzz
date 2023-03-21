from django.shortcuts import render
from login.forms import LoginForm
# Create your views here.

def landing_view(request, email, usertype):
	# data = request.GET.get('data',1)
	context = {
		'email': email,
		'usertype': usertype
	}
	return render(request, 'landing/landing.html', context)


# use if you want different landing pages for each type of user
# def student_view(request, *args, **kwargs):
# 	context = {}
# 	return render(request, 'landing/student.html', context)

# def professor_view(request, *args, **kwargs):
# 	context = {}
# 	return render(request, 'landing/professor.html', context)

# def admin_view(request, *args, **kwargs):
# 	context = {}
# 	return render(request, 'landing/admin.html', context)


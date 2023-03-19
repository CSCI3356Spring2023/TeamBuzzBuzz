from django.shortcuts import render
from django.contrib.auth.models import User
# from .forms import LoginForm
from .models import Login
from django.http import HttpResponse

# Create your views here.
def login_view(request, *args, **kwargs):
	# user = User.objects.get(email='abc@gmail.com')
	context = {
		'email': "example@gmail.com",
	}
	return render(request, 'login/login.html', context)

# def login_form_view(request):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()

# 	context = {
# 			'form': form
# 	}
# 	return render(request, '')

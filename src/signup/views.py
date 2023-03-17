from django.shortcuts import render

# Create your views here.
def signup_view(request, *args, **kwargs):
	context = {}
	return render(request, 'signup/signup.html', context)



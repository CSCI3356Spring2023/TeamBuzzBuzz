from django.shortcuts import render

# Create your views here.

def system_closed_view(request):
	return render(request, 'landing/system_closed.html')


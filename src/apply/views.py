from django.shortcuts import render
from .models import Apply
from .forms import ApplicationForm
# Create your views here.
def apply_form_view(request):
	form = ApplicationForm(request.POST or None) #register the object whenever it gets a request 
	if form.is_valid():
		form.save()
		form = ApplicationForm()

	context = {
			'form': form
	}
	return render(request, 'apply.html', context)
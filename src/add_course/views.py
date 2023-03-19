from django.shortcuts import render
from .forms import AddCourseForm
# Create your views here.
def add_course_view(request, *args, **kwargs):
    my_form = AddCourseForm()
    context = {
		"form" : my_form
	}
    return render(request, 'add_course/add_course.html', context)

# def course_confirmation(request, *args, **kwargs):
from django.shortcuts import render
from .forms import AddCourseForm
# Create your views here.
def add_course_view(request, *args, **kwargs):
    my_form = AddCourseForm()
    if request.method == "POST":
        my_form = AddCourseForm(request.POST or None)
        print("Posting Data")
        if my_form.is_valid():
            print("cleaned data: ", my_form.cleaned_data)
            my_form.save()
        else:
            print(my_form.errors)
        
        my_form = AddCourseForm()
    
    context = {
		"form" : my_form
	}
    return render(request, 'add_course/add_course.html', context)

# def course_confirmation(request, *args, **kwargs):
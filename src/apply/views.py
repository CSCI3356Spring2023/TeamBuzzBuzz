from django.shortcuts import render, redirect
from .forms import ApplicationForm
from add_course.models import Course
from django.contrib import messages

# add decorator to make this only accessible to students and admin
def apply_view(request, app_id):
    course_data = Course.objects.get(id=app_id)
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST or None)
        print("Posting Data")
        if form.is_valid():
            form.save()
            messages.success(request, f'Application submitted!')
            return redirect('course_list')
        else:
            print(form.errors)
        
        form = ApplicationForm()
    context = {
        'course' : course_data,
        'form' : form
    }
        
    return render(request, 'apply/apply.html', context)
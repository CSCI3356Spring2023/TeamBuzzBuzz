from django.shortcuts import render
from .forms import ApplicationForm
from add_course.models import Course

def apply_view(request, app_id):
    course_data = Course.objects.get(id=app_id)
    print(course_data)
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST or None)
        print("Posting Data")
        if form.is_valid():
            print("cleaned data: ", form.cleaned_data)
            form.save()
        else:
            print(form.errors)
        
        form = ApplicationForm()
    context = {
        'course' : course_data,
        'form' : form
    }
        
    return render(request, 'apply/apply.html', context)
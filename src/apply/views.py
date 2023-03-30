from django.shortcuts import render
from .forms import ApplicationForm
from add_course.models import Course

# add decorator to make this only accessible to students and admin
def apply_view(request, app_id):
    course_data = Course.objects.get(id=app_id)
    print(course_data)
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST or None)
        print("Posting Data")
        if form.is_valid():
            print("cleaned data: ", form.cleaned_data)
            application = form.save()
            application.course_title = course_data.course_title
            application.discussion = course_data.discussion
            application.description = course_data.description
            application.email = course_data.email
            application.ta_required = course_data.ta_required
            form.save()
        else:
            print(form.errors)
        
        form = ApplicationForm()
    context = {
        'course' : course_data,
        'form' : form
    }
        
    return render(request, 'apply/apply.html', context)
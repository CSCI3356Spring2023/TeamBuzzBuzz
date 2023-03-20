from django.shortcuts import render
from add_course.models import Course
# Create your views here.

def course_list_view(request):
    course_data = Course.objects.all()

    context = {
        'course_data' : course_data
    }

    return render(request, 'course_list/course_list.html', context)
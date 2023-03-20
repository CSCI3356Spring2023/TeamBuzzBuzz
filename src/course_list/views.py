from django.shortcuts import render
from add_course.models import CourseModel
# Create your views here.

def course_list_view(request):
    course_data = CourseModel.objects.all()

    context = {
        'course_data' : course_data
    }

    return render(request, 'course_list/course_list.html', context)
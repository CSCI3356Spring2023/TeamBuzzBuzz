from django.shortcuts import render, redirect, get_object_or_404
from add_oldcourse.models import Course
from student_oldcourse.models import OldCourse
from users.models import CustomUser
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist

class NormalCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'show_oldcourse/show_oldcourse.html'
    ordering = ['course_title']
    context_object_name = 'course_data'

    def save_old_course(request, **kwargs):
        sender = request.user
        course_id = kwargs.get('course_id', 0)
        print("course_id: ", course_id)
        course = Course.objects.get(id=course_id)
        studentoldcourse = OldCourse(course_title = course.course_title, year = course.year, semester = course.semester, author = course.author, taker = sender )
        studentoldcourse.save()
        return redirect('show_normaloldcourse')

class ProfessorOldCoursesView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'show_oldcourse/show_oldcourse.html'
    ordering = ['course_title']
    context_object_name = 'course_data'

    def get_queryset(self, *args, **kwargs):
        key = self.kwargs['pk']
        print("Key:", key)
        try:
            user = CustomUser.objects.get(pk=key)
            print("User:", user)
            courses = Course.objects.filter(author=user)
            print("Courses:", courses)
            return courses
        except ObjectDoesNotExist as e:
            print("Exception:", e)
            return Course.objects.none()


    # def get_queryset(self, *args, **kwargs):
    #     first, last = self.kwargs['name'].split("_")
    #     print("Name:", self.kwargs['name'], "First:", first, "Last:", last)
    #     try:
    #         user = CustomUser.objects.get(first_name__iexact=first, last_name__iexact=last)
    #         print("User:", user)
    #         courses = Course.objects.filter(author=user)
    #         print("Courses:", courses)
    #         return courses
    #     except ObjectDoesNotExist as e:
    #         print("Exception:", e)
    #         return Course.objects.none()

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filtered'] = True
        return context
    
    


# @login_required
# def course_list_view(request):
#     course_data = Course.objects.all()

#     context = {
#         'course_data' : course_data,
#         'all_courses' : True
#     }

#     return render(request, 'course_list/course_list.html', context)



